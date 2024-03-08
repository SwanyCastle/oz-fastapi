from fastapi import FastAPI, APIRouter


BOOKS = [
    {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "url": "https://example.com/1984",
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "url": "https://example.com/to-kill-a-mockingbird",
    },
    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "url": "https://example.com/the-great-gatsby",
    },
]

app = FastAPI()
router = APIRouter()

@router.get('/', status_code=200)
def main() -> dict:
    return { "message": "Welcome to the game world!"}

@router.get('/books', status_code=200)
def fetch_books() -> list:
    return BOOKS

@router.get('/books/{book_id}', status_code=200)
def fetch_book(book_id: int) -> dict:
    # for book in BOOKS:
    #     if book['id'] == book_id:
    #         return book
    # return {"error": "NotFound"}
    book = next((book for book in BOOKS if book["id"] == book_id), None)
    if book:
        return book
    return {"error": "Book Not Found"}

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("books:app", reload=True, log_level='info')