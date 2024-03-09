# pydantic - django 의 serializer 와 비슷한 기능
# 뭔가 model 이랑 serializer 랑 섞여 있는 느낌
from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID


class Book(BaseModel):
    id: UUID
    title: str
    author: str
    # description 은 str 이될 수도 있고 None 이 될 수도 있도록 Optional 로 설정
    description: Optional[str] = None


class CreateBook(BaseModel):
    title: str
    author: str
    # description 은 str 이될 수도 있고 None 이 될 수도 있도록 Optional 로 설정
    description: Optional[str] = None


class BookSearch(BaseModel):
    # results: Sequence[Book]
    results: Optional[Book]


class SearchResultBook(BaseModel):
    results: List[Book]