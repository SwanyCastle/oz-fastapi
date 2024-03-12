import crud, dependencies, schemas
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Union

router = APIRouter(prefix="/api/v1/users", tags=["User"])

@router.get('/')
def get_user(skip: int, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    users = crud.get_user_list(skip=skip, limit=limit, db=db)
    return (users)

@router.get('/{user_data}')
def get_user_id(user_data: Union[int, str], db: Session = Depends(dependencies.get_db)):
    db_user = crud.get_user(db, user_data)
    return dependencies.is_None(db_user)

# @router.get('/{user_email}')
# def get_user_id(user_email: str, db: Session = Depends(dependencies.get_db)):
#     db_user = crud.get_user_email(user_email=user_email, db=db)
#     return dependencies.is_None(db_user)

@router.post('/', response_model=schemas.User)
def create_user(user: schemas.CreateUser, db: Session = Depends(dependencies.get_db)) -> schemas.User:
    db_user = crud.create_user(db, user)
    return db_user

@router.put('/{user_id}')
def update_user(user_id: int, user: schemas.UpdateUser, db: Session = Depends(dependencies.get_db)):
    updated_user = crud.update_user(db, user_id, user)
    return dependencies.is_None(updated_user)

@router.delete('/{user_id}')
def delete_user(user_id: int, db: Session = Depends(dependencies.get_db)):
    deleted_user = crud.delete_user(db, user_id)
    return dependencies.is_None(deleted_user)

# 순서가 중요한듯 
# create_item 함수 인자에서 path param 이 먼저
@router.post('/{user_id}/items', response_model=schemas.Item)
def create_item(user_id: int, item: schemas.CreateItem, db: Session = Depends(dependencies.get_db)) -> schemas.Item:
    db_item = crud.create_item(db, item, user_id=user_id)
    return db_item