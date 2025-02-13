# apps/models.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base
import uuid


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    file_id = Column(String, unique=True, index=True, default=lambda: str(uuid.uuid4()))  # 唯一文件ID
    created_at = Column(DateTime, default=func.now())  # 创建时间
