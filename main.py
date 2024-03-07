from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {'Hello World!'}

# http://127.0.0.1:5000/items/3?query=asdasd - query 넣고싶은 경우
@app.get('/items/{item_id}')
def read_item(item_id: int, query: str=None) -> dict:
    data = {'item_id': item_id, 'query': query}
    return data



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=5000, log_level="debug", reload=True)