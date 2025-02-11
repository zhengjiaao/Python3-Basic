from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "test_users"
    # __table_args__ = {'schema': 'public'}  # 指定模式

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)