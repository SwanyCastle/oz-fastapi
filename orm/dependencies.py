from database import SessionLocal
from database import AsyncSessionLocal

# 동기처리 의존성
def get_db():
    db = SessionLocal()

    try:
        # 세션연결 기간동안 연결을 유지하게 해줌
        yield db
    finally:
        db.close()

# 비동기처리 의존성
async def get_async_db():
    # 세션을 AsyncSessionLocal 가 알아서 관리 해주기 떄문에 
    # try, finally 필요 없음
    # db 에서의 세션 연결이 중요한 이유는 연결이 많으면 많을 수록 서버에 부하가 걸림
    # django 에서는 세선관리가 기본적으로 제공이 됨
    async with AsyncSessionLocal() as session:
        # 세션연결 기간동안 연결을 유지하게 해줌
        yield session