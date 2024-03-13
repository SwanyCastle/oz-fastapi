from models import User
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import Union
from schemas import userSchema
import bcrypt


# Get User
# skip, limit -> 페이지네이션
def get_user_list(db: Session, skip: int=0, limit: int = 10) -> userSchema.User:
    user_list_sql = text("SELECT * FROM users LIMIT :limit OFFSET :skip")
    results = db.execute(user_list_sql, {"limit": limit, "skip": skip}).fetchall()
    return [row._asdict() for row in results]

def get_user(db: Session, user_data: Union[int, str]) -> userSchema.User:
    try:
        user_data = int(user_data)
        if isinstance(user_data, int):
            userId_sql = text("SELECT * FROM users WHERE id = :user_data")
            result = db.execute(userId_sql, {"user_data": user_data}).fetchone()
            return result._asdict()
    except:
        if isinstance(user_data, str):
            userEmail_sql = text("SELECT * FROM users WHERE id = :user_data")
            result = db.execute(userEmail_sql, {"user_data": user_data}).fetchone()
            return result._asdict()


# Create User
def create_user(db: Session, user: userSchema.CreateUser) -> userSchema.User:
    hashed_password = bcrypt.hashpw(user.hashed_password.encode('utf-8'), bcrypt.gensalt())

    insert_sql = text("INSERT INTO users(email, hashed_password) VALUES (:email, :hashed_password)")

    db.execute(insert_sql, {"email": user.email, "hashed_password": hashed_password})
    db.commit()

    # 잘 만들어 졌는지 확인 -> 방금 만든 유저의 아이디를 가져옴
    # LAST_INSERT_ID -> 가장 마지막에 생성된 유저 이이디 가져오는 sql 함수
    select_sql = text("SELECT LAST_INSERT_ID()")
    result = db.execute(select_sql)
    # 파이썬이 이해하도록 변환
    user_id = result.scalar()
    return get_user(db, user_id)


# Update User
def update_user(db: Session, user_id: int, user_update: userSchema.UpdateUser) -> userSchema.User:
    user_data = user_update.model_dump()

    data = ", ".join([f"{key} = :{key}" for key, value in user_data.items()])
    
    update_sql = text(f"UPDATE users SET {data} WHERE id = :user_id")
    user_data["user_id"] = user_id
    db.execute(update_sql, user_data)
    db.commit()

    return get_user(db, user_id)

# Delete User
def delete_user(db: Session, user_id: int) -> userSchema.User:
    delete_sql = text("DELETE FROM users WHERE id = :user_id")
    db.execute(delete_sql, {"user_id": user_id})
    db.commit()
    return get_user(db, user_id)

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