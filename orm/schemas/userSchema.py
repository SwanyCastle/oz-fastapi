from pydantic import BaseModel
from typing import List, Optional
from schemas.itemSchema import Item


class UserBase(BaseModel):
    email: str


class User(UserBase):
    id: int
    # items: List[Item] = []
    items: Optional[List[Item]] = []

    class Config:
        orm_mode = True


class CreateUser(UserBase):
    hashed_password: str


class UpdateUser(UserBase):
    #  | (or 문법) 은 python 3.10 이상부터 사용가능
    email: str | None = None
    hashed_password: str  | None = None


# raise fastapi.exceptions.FastAPIError(
#     fastapi.exceptions.FastAPIError: 
#     Invalid args for response field! Hint: check that <class 'models.User'> 
#     is a valid Pydantic field type. 
#     If you are using a return type annotation that is not a valid 
#     Pydantic field (e.g. Union[Response, dict, None]) you can disable generating 
#     the response model from the type annotation with the path operation decorator 
#     parameter response_model=None. Read more: https://fastapi.tiangolo.com/tutorial/response-model/