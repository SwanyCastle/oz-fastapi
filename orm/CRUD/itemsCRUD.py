from models import Item
from sqlalchemy.orm import Session
from typing import Union
from schemas import itemSchema


# Get Item
# Limit: 10 ~ 100 정도
def get_item_list(db: Session, skip: int=0, limit: int = 10) -> itemSchema.Item:
    return db.query(Item).offset(skip).limit(limit).all()

def get_item(db: Session, item_data: Union[int, str]) -> itemSchema.Item:
    try:
        item_data = int(item_data)
        if isinstance(item_data, int):
            return db.query(Item).filter(Item.id == item_data).first()
    except:
        if isinstance(item_data, str):
            return db.query(Item).filter(Item.title == item_data).first()

# Create Item
def create_item(db: Session, item: itemSchema.CreateItem, owner_id: int) -> itemSchema.Item:
    # item = Item(title=item.title, description=item.description, owner_id=owner_id)
    db_item = Item(**item.model_dump(), owner_id=owner_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Update Item
def update_item(db: Session, item_id: int, item_data: itemSchema.UpdateItem) -> itemSchema.Item:
    db_item = db.query(Item).filter(Item.id == item_id).first()

    if db_item is None:
        return None

    for key, value in item_data.model_dump().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

# Delete Item
def delete_item(db: Session, item_id: int) -> itemSchema.Item:
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        return None
    db.delete(db_item)
    db.commit()
    return db_item
    # return {"msg": "Successfully Deleted Item"}

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


# sqlalchemy.exc.ArgumentError: 
# Column expression, 
# FROM clause, or other columns clause element expected, got <class 'schemas.itemSchema.Item'>.