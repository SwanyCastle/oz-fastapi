# db 랑 연결하는 것을 정의하는 코드
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 동기용 데이터 베이스 설정
SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:root@localhost/oz_fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# FastAPI 를 쓰는 중요한 특징 중 하나가 비동기처리
# (1) 비동기 방식 - Starlette
# (2) 데이터 검증 - pydantic

# 이걸 사용하면 fastapi 의 특징인 비동기 처리를 동기로 처리할 수 밖에 없다
# (파이썬이 기본적으로 동기적임)
# 따라서 db 도 비동기 처리 할 수 있도록 따로 설정해줘야한다
# SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:root@localhost/oz_fastapi"

# aiomysql -> 비동기로 처리할 수 있도록 하는 라이브러리
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

ASYNC_SQLALCHEMY_DATABASE_URL = "mysql+aiomysql://root:root@localhost/oz_fastapi"
async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)
AsyncSessionLocal = sessionmaker(bind=async_engine, class_=AsyncSession)

Base = declarative_base()