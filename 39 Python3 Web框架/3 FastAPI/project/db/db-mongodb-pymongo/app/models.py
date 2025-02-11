# models.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from bson import ObjectId


class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

    class Config:
        populate_by_name = True  # 替换原来的 allow_population_by_field_name


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: str = Field(..., alias="_id")

    class Config:
        populate_by_name = True  # 替换原来的 allow_population_by_field_name
        json_encoders = {
            ObjectId: str
        }
