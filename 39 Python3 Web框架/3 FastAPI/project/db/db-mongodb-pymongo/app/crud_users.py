# app/crud_users.py
from . import schemas  # 使用相对导入,同级目录下
from . import models  # 使用相对导入,同级目录下
from bson import ObjectId
from typing import List, Optional
from . import database


def get_db():
    return database.database


def get_user_by_email(email: str) -> Optional[models.User]:
    user_dict = get_db().users.find_one({"email": email})
    if user_dict:
        user_dict['id'] = str(user_dict.pop('_id'))  # 将 _id 转换为 id 字符串
        return models.User(**user_dict)
    return None


def get_user(user_id: str) -> Optional[models.User]:
    user_dict = get_db().users.find_one({"_id": ObjectId(user_id)})
    if user_dict:
        user_dict['id'] = str(user_dict.pop('_id'))  # 将 _id 转换为 id 字符串
        return models.User(**user_dict)
    return None


def get_users(skip: int = 0, limit: int = 10) -> List[models.User]:
    users_cursor = get_db().users.find().skip(skip).limit(limit)
    users_list = []
    for user_dict in users_cursor:
        user_dict['id'] = str(user_dict.pop('_id'))  # 将 _id 转换为 id 字符串
        users_list.append(models.User(**user_dict))
    return users_list


def create_user(user: models.UserCreate) -> models.User:
    user_dict = user.dict()
    result = get_db().users.insert_one(user_dict)
    created_user = get_db().users.find_one({"_id": result.inserted_id})
    if created_user:
        created_user['id'] = str(created_user.pop('_id'))  # 将 _id 转换为 id 字符串
        return models.User(**created_user)
    raise ValueError("User creation failed")


def update_user(user_id: str, user_update: models.UserBase) -> Optional[models.User]:
    result = get_db().users.update_one({"_id": ObjectId(user_id)}, {"$set": user_update.dict(exclude_unset=True)})
    if result.modified_count == 1:
        updated_user = get_db().users.find_one({"_id": ObjectId(user_id)})
        if updated_user:
            updated_user['id'] = str(updated_user.pop('_id'))  # 将 _id 转换为 id 字符串
            return models.User(**updated_user)
    return None


def delete_user_v1(user_id: str) -> Optional[bool]:
    result = get_db().users.delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count == 1


def delete_user_v2(user_id: str) -> Optional[models.User]:
    user_dict = get_db().users.find_one_and_delete({"_id": ObjectId(user_id)})
    if user_dict:
        user_dict['id'] = str(user_dict.pop('_id'))  # 将 _id 转换为 id 字符串
        return models.User(**user_dict)
    return None
