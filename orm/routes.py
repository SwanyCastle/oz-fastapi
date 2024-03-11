import crud, dependencies, schemas
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/v1/users", tags=["User"])

@router.get('/', response_model=schemas.User)
def get_user(db: Session = Depends(dependencies.get_db)):
    db_user_list = crud.read_user_list(db)
    serializers = [schemas.User(id=user.id, email=user.email, items=user.items).model_dump() for user in db_user_list]
    return JSONResponse(content=serializers)

@router.post('/', response_model=schemas.User)
def create_user(user: schemas.CreateUser, db: Session = Depends(dependencies.get_db)) -> schemas.User:
    db_user = crud.create_user(db, user)
    return db_user

# 순서가 중요한듯 
# path param 이 먼저 오는듯?
@router.post('/{user_id}/items', response_model=schemas.Item)
def create_item(user_id: int, item: schemas.CreateItem, db: Session = Depends(dependencies.get_db)) -> schemas.Item:
    db_item = crud.create_item(db, item, user_id=user_id)
    return db_item