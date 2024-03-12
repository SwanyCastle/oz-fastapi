from models import User, Item
from sqlalchemy.orm import Session
from typing import Union
import schemas
import bcrypt


# Create User
def create_user(db: Session, user: schemas.CreateUser) -> schemas.User:
    hashed_password = bcrypt.hashpw(user.hashed_password.encode('utf-8'), bcrypt.gensalt())

    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    return db_user

# Read User
# skip, limit -> 페이지네이션
def get_user_list(db: Session, skip: int=0, limit: int = 10) -> schemas.User:
    return db.query(User).offset(skip).limit(limit).all()

def get_user(db: Session, user_data: Union[int, str]) -> schemas.User:
    try:
        user_data = int(user_data)
        if isinstance(user_data, int):
            return db.query(User).filter(User.id == user_data).first()
    except:
        if isinstance(user_data, str):
            return db.query(User).filter(User.email == user_data).first()

# def get_user_email(db: Session, user_email: str) -> schemas.User:
#     return db.query(User).filter(User.email == user_email).first()

# Update User
def update_user(db: Session, user_id: int, user_update: schemas.UpdateUser) -> schemas.User:
    hashed_password = bcrypt.hashpw(user_update.hashed_password.encode('utf-8'), bcrypt.gensalt())
    user_update.hashed_password = hashed_password

    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    update_data = user_update.model_dump()

    for key, value in update_data.items():
        # setattr() 업데이트 할 때 사용 
        setattr(db_user, key, value)
    db.commit()
    # 커밋을 했지만 db 가 최신 데이터로 업데이트 되어있지 않을 수도 있기에 
    # refresh 사용
    db.refresh(db_user)
    return db_user

# Delete User
def delete_user(db: Session, user_id: int) -> schemas.User:
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user

# -----------------------------------------------------------------------------------------------------------

# create item
def create_item(db: Session, item: schemas.CreateItem, user_id: int):
    item = Item(title=item.title, description=item.description, owner_id=user_id)
    db.add(item)
    db.commit()
    return item

# 직력화 못해줘서 나온 에러
# router 에다가 response_model 설정해 줘서 에러 난듯
# ResponseValidationError(
#     fastapi.exceptions.ResponseValidationError: 1 validation errors:
#         {
#             'type': 'model_attributes_type', 
#             'loc': ('response',), 
#             'msg': 'Input should be a valid dictionary or object to extract fields from', 
#             'input': [<models.User object at 0x1056b3320>, <models.User object at 0x1056400b0>], 
#             'url': 'https://errors.pydantic.dev/2.6/v/model_attributes_type'
#         }
# )

# CRUD + JWT Auth (기본) -> 추가로 채팅, 스트리밍(영상), 그래프용 데이터
# - SQL 방식 ORM 방식 둘다 알고 가야함
# - 위치 기반 -> 네이버 지도 API / 카카오 로그인 (OAuth2) 및 네이버, 구글 로그인 등
# - 기술은 매일 바뀜 -> 내가 찾아보고 공부해서 적용하는 프로세스를 할 줄 알아야함