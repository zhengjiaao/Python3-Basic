# app/schemas.py
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class FileBase(BaseModel):
    filename: str

class FileCreate(FileBase):
    data: bytes

class File(FileBase):
    id: int

    class Config:
        orm_mode = True
