from fastapi import FastAPI
from routes.books import router as book_router
from routes.movies import router as movie_router

app = FastAPI()

app.include_router(book_router, prefix='/api/v1/books')
# tags -> swagger-ui 에서 잘 활용하기위해 잘 구분하기위해 잘 알아보기위해 ?
app.include_router(movie_router, prefix='/api/v1/movies', tags=['Movies'])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, log_level="debug", reload=True)