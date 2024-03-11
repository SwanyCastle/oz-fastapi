# User, Itme(Feed)
# pydantic 에서 불러운 BaseModel 은 데이터 검증이 목적
# from pydantic import BaseModel
# database 의 Base 는 db 연결 목적
from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)

    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

# owner_id = Column(Integer, ForeignKey("users.id"))
# 아래꺼로 해서 오류 남
# owner_id = Column(Integer, ForeignKey("User.id"))
# sqlalchemy.exc.NoForeignKeysError: 
#     Could not determine join condition between parent/child tables on relationship 
#     User.items - there are no foreign keys linking these tables. 
#     Ensure that referencing columns are associated 
#     with a ForeignKey or ForeignKeyConstraint, or specify a 'primaryjoin' expression.