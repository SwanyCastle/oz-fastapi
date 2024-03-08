from fastapi import FastAPI
from routes import router as book_router

app = FastAPI()

app.include_router(book_router, prefix='/api/v1/books')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, log_level="debug", reload=True)