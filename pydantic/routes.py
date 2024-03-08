# 프로젝트 구조 
# models
# - item.py
# - users.py
# routes
# - items.py
# - users.py
from fastapi import APIRouter, HTTPException
from uuid import uuid4, UUID
from models import Book, CreateBook
from typing import List

router = APIRouter()
books: List[Book] = []

# /api/v1/books [POST]
@router.post('/')
def create_book(book_data: CreateBook) -> Book:
    # **book_data -> 유저(프론트엔드)가 만들어서 보낸 데이터
    # ** -> 이표시는 나머지 객체 데이터들을 포함해서 담아달라는 뜻 -> 객체 데이터를 한방에 불러오기위해 사용
    book = Book(id=uuid4(), **book_data.__dict__)
    books.append(book)
    return book

# /api/v1/books/{book_id} [GET]
@router.get('/{book_id}')
def get_book(book_id: UUID) -> Book:
    book = next((book for book in books if book.id==book_id), None)
    if not book:
        raise HTTPException(status_code=404)
    return book