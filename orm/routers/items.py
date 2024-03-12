import dependencies

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Union, List

from CRUD import itemsCRUD
from schemas.itemSchema import Item, CreateItem, UpdateItem

router = APIRouter(prefix="/api/v1/items", tags=["Item"])

@router.get('/')
# def get_item_list(skip: int, limit: int = 10, db: Session = Depends(dependencies.get_db)) -> Item: -> 이거 하면 ValidaionError 남 ㅡ.ㅡ 개열받네
# def get_item_list(skip: int, limit: int = 10, db: Session = Depends(dependencies.get_db)) -> List[Item]: -> 이거하면 ResponseValidationError: 1 validation errors: {'type': 'int_type', 'loc': ('response', 9, 'owner_id'), 'msg': 'Input should be a valid integer', 'input': None, 'url': 'https://errors.pydantic.dev/2.6/v/int_type'}
def get_item_list(skip: int, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    db_items = itemsCRUD.get_item_list(skip=skip, limit=limit, db=db)
    return dependencies.is_None(db_items)

@router.get('/{item_data}')
def get_item(item_data: Union[int, str], db: Session = Depends(dependencies.get_db)) -> Item:
    db_item = itemsCRUD.get_item(db, item_data)
    return dependencies.is_None(db_item)

# 순서가 중요한듯 
# create_item 함수 인자에서 path param 이 먼저
@router.post('/{owner_id}', response_model=Item)
def create_item(owner_id: int, item: CreateItem, db: Session = Depends(dependencies.get_db)) -> Item:
    db_item = itemsCRUD.create_item(db, item, owner_id)
    return dependencies.is_None(db_item)

@router.put('/{item_id}')
def update_item(item_id: int, item: UpdateItem, db: Session = Depends(dependencies.get_db)) -> Item:
    updated_item = itemsCRUD.update_item(db, item_id, item)
    return dependencies.is_None(updated_item)

@router.delete('/{item_id}')
def delete_item(item_id: int, db: Session = Depends(dependencies.get_db)) -> Item:
    deleted_item = itemsCRUD.delete_item(db, item_id)
    return dependencies.is_None(deleted_item)