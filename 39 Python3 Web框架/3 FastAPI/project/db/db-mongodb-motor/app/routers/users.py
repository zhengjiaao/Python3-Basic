# app/routers/users.py

from fastapi import APIRouter, Depends, HTTPException
from .. import crud
from motor.motor_asyncio import AsyncIOMotorClient
from .. import database
from ..models import User, UserCreate, UserBase  # 导入 User,UserCreate模型

router = APIRouter()


def get_db():
    return database.database


@router.post("/users/", response_model=User)
async def create_user_endpoint(user: UserCreate, db: AsyncIOMotorClient = Depends(get_db)):
    db_user = await crud.get_user_by_email(db, email=str(user.email))
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await crud.create_user(db, user)


@router.get("/users/", response_model=list[User])
async def read_users(skip: int = 0, limit: int = 10, db: AsyncIOMotorClient = Depends(get_db)):
    users = await crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: str, db: AsyncIOMotorClient = Depends(get_db)):
    db_user = await crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User not found")
    return db_user


@router.put("/users/{user_id}", response_model=User)
async def update_user_endpoint(user_id: str, user_update: UserBase, db: AsyncIOMotorClient = Depends(get_db)):
    db_user = await crud.update_user(db, user_id=user_id, user_update=user_update)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User not found")
    return db_user


@router.delete("/users/delete/v1/{user_id}", response_model=bool)
async def delete_user_endpoint(user_id: str, db: AsyncIOMotorClient = Depends(get_db)):
    result = await crud.delete_user_v1(db, user_id=user_id)
    if result is None:
        raise HTTPException(status_code=400, detail="User not found")
    return True


@router.delete("/users/delete/v2/{user_id}", response_model=User)
async def delete_user_v2_endpoint(user_id: str, db: AsyncIOMotorClient = Depends(get_db)):
    db_user = await crud.delete_user_v2(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User not found")
    return db_user
