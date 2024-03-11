from pydantic import BaseModel
from typing import List


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class CreateItem(ItemBase):
    pass


class UpdateItem(ItemBase):
    title: str | None = None
    description: str | None = None


class UserBase(BaseModel):
    email: str


class User(UserBase):
    id: int
    # items: List[Item] = None

    class Config:
        orm_mode = True


class CreateUser(UserBase):
    hashed_password: str


class UpdateUser(UserBase):
    #  | (or 문법) 은 python 3.10 이상부터 사용가능
    email: str | None = None
    hashed_password: str  | None = None
