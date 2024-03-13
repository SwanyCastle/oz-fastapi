from models import Item
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import Union
from schemas import itemSchema


# Get Item
# Limit: 10 ~ 100 정도
def get_item_list(db: Session, skip: int=0, limit: int = 10) -> itemSchema.Item:
    item_list_sql = text("SELECT * FROM items LIMIT :limit OFFSET :skip")
    results = db.execute(item_list_sql, {"limit": limit, "skip": skip}).fetchall()
    return [row._asdict() for row in results]

def get_item(db: Session, item_data: Union[int, str]) -> itemSchema.Item:
    try:
        item_data = int(item_data)
        if isinstance(item_data, int):
            item_id_sql = text("SELECT * FROM items WHERE id = :item_data")
            result = db.execute(item_id_sql, {"item_data": item_data}).fetchone()
            return result._asdict()
    except:
        if isinstance(item_data, str):
            item_id_sql = text("SELECT * FROM items WHERE id = :item_data")
            result = db.execute(item_id_sql, {"item_data": item_data}).fetchone()
            return result._asdict()

# Create Item
def create_item(db: Session, item: itemSchema.CreateItem, owner_id: int) -> itemSchema.Item:
    create_data = item.model_dump()
    create_data["owner_id"] = owner_id

    insert_sql = text("INSERT INTO items(title, description, owner_id) VALUES (:title, :description, :owner_id)")
    db.execute(insert_sql, create_data)
    db.commit()

    select_sql = text("SELECT LAST_INSERT_ID()")
    new_item_id = db.execute(select_sql)
    new_item_id.scalar()

    return get_item(db, new_item_id)



# Update Item
def update_item(db: Session, item_id: int, item_update: itemSchema.UpdateItem) -> itemSchema.Item:
    item_data = item_update.model_dump()

    data = ", ".join([f"{key} = :{key}" for key, value in item_data.items()])
    
    update_sql = text(f"UPDATE items SET {data} WHERE id = :item_id")
    item_data["item_id"] = item_id

    print(update_sql)

    db.execute(update_sql, item_data)
    db.commit()

    return get_item(db, item_id)

# Delete Item
def delete_item(db: Session, item_id: int) -> itemSchema.Item:
    delete_sql = text("DELETE FROM items WHERE id = :item_id")
    db.execute(delete_sql, {"item_id": item_id})
    db.commit()
    return get_item(db, item_id)

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