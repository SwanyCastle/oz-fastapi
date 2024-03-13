import dependencies

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Union, List

from CRUD import usersCRUD, users_sqlquery
from schemas.userSchema import CreateUser, UpdateUser, User

router = APIRouter(prefix="/api/v1/users", tags=["User"])

# ORM 버전
# @router.get('/')
# def get_user_list(skip: int, limit: int = 10, db: Session = Depends(dependencies.get_db)) -> List[User]:
#     users = usersCRUD.get_user_list(skip=skip, limit=limit, db=db)
#     return dependencies.is_None(users)

# @router.get('/{user_data}')
# def get_user(user_data: Union[int, str], db: Session = Depends(dependencies.get_db)) -> User:
#     db_user = usersCRUD.get_user(db, user_data)
#     return dependencies.is_None(db_user)

# @router.get('/{user_email}')
# def get_user_id(user_email: str, db: Session = Depends(dependencies.get_db)):
#     db_user = crud.get_user_email(user_email=user_email, db=db)
#     return dependencies.is_None(db_user)

# @router.put('/{user_id}')
# def update_user(user_id: int, user: UpdateUser, db: Session = Depends(dependencies.get_db)) -> User:
#     updated_user = usersCRUD.update_user(db, user_id, user)
#     return dependencies.is_None(updated_user)

# @router.delete('/{user_id}')
# def delete_user(user_id: int, db: Session = Depends(dependencies.get_db)) -> User:
#     deleted_user = usersCRUD.delete_user(db, user_id)
#     return dependencies.is_None(deleted_user)

# SQL Query 버전
@router.get('/')
def get_user_list(skip: int, limit: int = 10, db: Session = Depends(dependencies.get_db)) -> List[User]:
    users = users_sqlquery.get_user_list(skip=skip, limit=limit, db=db)
    return dependencies.is_None(users)


@router.get('/{user_data}')
def get_user(user_data: Union[int, str], db: Session = Depends(dependencies.get_db)) -> User:
    db_user = users_sqlquery.get_user(db, user_data)
    return dependencies.is_None(db_user)


@router.post('/', response_model=User)
def create_user(user: CreateUser, db: Session = Depends(dependencies.get_db)) -> User:
    db_user = usersCRUD.create_user(db, user)
    return dependencies.is_None(db_user)


@router.put('/{user_id}')
def update_user(user_id: int, user: UpdateUser, db: Session = Depends(dependencies.get_db)) -> User:
    updated_user = users_sqlquery.update_user(db, user_id, user)
    return dependencies.is_None(updated_user)


@router.delete('/{user_id}')
def delete_user(user_id: int, db: Session = Depends(dependencies.get_db)) -> User:
    deleted_user = users_sqlquery.delete_user(db, user_id)
    return dependencies.is_None(deleted_user)