# FastAPI

### 1. 가상환경 구축
> python -m venv .venv
> source .venv/bin/activate

### 2. 라이브러리 설치
> pip install fastapi && pip install "uvicorn[standard]"
> pip install "fastapi[all]"

### 3. 실행 방법
> uvicorn main:app --reload

> python main.py 로 실행
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=5000, log_level="debug", reload=True)