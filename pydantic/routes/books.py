from fastapi import APIRouter, HTTPException
from uuid import uuid4, UUID
from models.book import Book, CreateBook, SearchResultBook
from typing import List, Optional

router = APIRouter()
books: List[Book] = []

# /api/v1/books [POST]
@router.post('/')
def create_book(book_data: CreateBook) -> Book:
    # **book_data -> 유저(프론트엔드)가 만들어서 보낸 데이터
    # ** -> 이표시는 나머지 객체 데이터들을 포함해서 담아달라는 뜻 -> 객체 데이터를 한방에 불러오기위해 사용
    book = Book(id=uuid4(), **book_data.model_dump())
    books.append(book)
    return book

# /api/v1/books [GET]
# @router.get('/')
# def get_book() -> List[Book]:
#     return books

# /api/v1/books/{book_id} [GET]
@router.get('/{book_id}')
def get_book(book_id: UUID) -> Book:
    book = next((book for book in books if book.id==book_id), None)
    if not book:
        raise HTTPException(status_code=404)
    return book

# pathParam -> {book_id}
# queryParam -> search?keyword={book_id}
# /api/v1/books/search [GET]
@router.get('/search/', response_model=SearchResultBook)
def search_book(keyword: Optional[str] = None, max_results: int = 10) -> SearchResultBook:
    result = [book for book in books if keyword.lower() in book.title.lower()] if keyword else books
    return SearchResultBook(results=result[:max_results])

