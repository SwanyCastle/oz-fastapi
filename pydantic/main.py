from fastapi import FastAPI
from routes.books import router as book_router
from routes.movies import router as movie_router

app = FastAPI()

app.include_router(book_router, prefix='/api/v1/books')
app.include_router(movie_router, prefix='/api/v1/movies')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, log_level="debug", reload=True)