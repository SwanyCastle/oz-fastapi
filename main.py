from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {'Hello World!'}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=5000, log_level="debug", reload=True)