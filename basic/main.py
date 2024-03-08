from fastapi import FastAPI
from items import router as items_router
from basic.users import router as users_router

app = FastAPI()

app.include_router(items_router)
app.include_router(users_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, log_level="debug", reload=True)