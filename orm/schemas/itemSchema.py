from pydantic import BaseModel


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