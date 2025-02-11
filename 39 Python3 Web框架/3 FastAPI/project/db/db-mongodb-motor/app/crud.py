# app/files.py
from motor.motor_asyncio import AsyncIOMotorClient
from .models import User, UserCreate, UserBase
from . import schemas
from bson import ObjectId
from datetime import datetime, timezone
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 明确指定集合名称
USERS_COLLECTION = "users"


async def create_user(db: AsyncIOMotorClient, user: UserCreate):
    try:
        user_dict = user.model_dump()  # 使用 model_dump 替代 dict
        user_dict["hashed_password"] = user_dict.pop("password")  # 假设你有一个哈希密码的方法
        result = await db[USERS_COLLECTION].insert_one(user_dict)
        created_user = await db[USERS_COLLECTION].find_one({"_id": result.inserted_id})

        # 将 _id 转换为字符串
        if created_user:
            logger.info(f"Created user: {created_user}")
            created_user["_id"] = str(created_user["_id"])

        return User(**created_user) if created_user else None
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        raise


async def get_user(db: AsyncIOMotorClient, user_id: str):
    user = await db.users.find_one({"_id": ObjectId(user_id)})
    # user = await db[USERS_COLLECTION].find_one({"_id": ObjectId(user_id)})
    if user:
        logger.info(f"get_user: {user}")
        user["_id"] = str(user["_id"])
        return User(**user)
    return None


async def get_user_by_email(db: AsyncIOMotorClient, email: str):
    user = await db.users.find_one({"email": email})
    if user:
        logger.info(f"Created user: {user}")
        user["_id"] = str(user["_id"])
        return User(**user)
    return None


async def get_users(db: AsyncIOMotorClient, skip: int = 0, limit: int = 10):
    users = []
    async for user in db.users.find().skip(skip).limit(limit):
        user["_id"] = str(user["_id"])
        users.append(User(**user))
    return users


async def update_user(db: AsyncIOMotorClient, user_id: str, user_update: UserBase):
    update_data = user_update.model_dump(exclude_unset=True)  # 使用 model_dump 替代 dict
    result = await db.users.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
    logger.info(f"update_user modified_count: {result.modified_count}")
    if result.modified_count == 1:
        updated_user = await db.users.find_one({"_id": ObjectId(user_id)})
        updated_user["_id"] = str(updated_user["_id"])
        return User(**updated_user)
    return None


async def delete_user_v1(db: AsyncIOMotorClient, user_id: str):
    result = await db.users.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 1:
        return True
    return False


async def delete_user_v2(db: AsyncIOMotorClient, user_id: str):
    # 先查询用户信息
    user = await db[USERS_COLLECTION].find_one({"_id": ObjectId(user_id)})
    if not user:
        return None  # 用户不存在

    # 删除用户
    result = await db[USERS_COLLECTION].delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 1:
        # 将 _id 转换为字符串
        user["_id"] = str(user["_id"])
        return User(**user)  # 返回删除前的用户信息
    return None


# 明确指定集合名称
FILES_COLLECTION = "files"


# 文件上传
async def upload_file(db: AsyncIOMotorClient, file: schemas.FileUpload):
    file_dict = file.model_dump(exclude_unset=True)
    file_dict["uploaded_at"] = datetime.now(timezone.utc)  # 使用时区感知的时间对象
    file_dict["file_size"] = len(file.content)  # 添加文件大小
    result = await db[FILES_COLLECTION].insert_one(file_dict)
    uploaded_file = await db[FILES_COLLECTION].find_one({"_id": result.inserted_id})

    # 将 _id 转换为字符串并映射为 id
    if uploaded_file:
        uploaded_file["id"] = str(uploaded_file.pop("_id"))
        # 仅保留需要的字段
        uploaded_file = {
            "id": uploaded_file["id"],
            "filename": uploaded_file["filename"],
            "file_size": uploaded_file["file_size"],
            "uploaded_at": uploaded_file["uploaded_at"]
        }
        return schemas.File(**uploaded_file)
    return None


# 获取文件信息
async def get_file(db: AsyncIOMotorClient, id: str):
    file = await db[FILES_COLLECTION].find_one({"_id": ObjectId(id)})
    if file:
        file["id"] = str(file.pop("_id"))
        # 仅保留需要的字段
        file = {
            "id": file["id"],
            "filename": file["filename"],
            "file_size": file["file_size"],
            "uploaded_at": file["uploaded_at"]
        }
        return schemas.File(**file)
    return None


# 获取文件列表
async def get_files(db: AsyncIOMotorClient, skip: int = 0, limit: int = 10):
    files = []
    async for file in db[FILES_COLLECTION].find().skip(skip).limit(limit):
        file["id"] = str(file.pop("_id"))
        # 检查并设置默认值
        file.setdefault("file_size", 0)  # 如果没有 file_size 字段，则设置为 0
        # 仅保留需要的字段
        file_info = {
            "id": file["id"],
            "filename": file.get("filename", ""),
            "file_size": file["file_size"],
            "uploaded_at": file.get("uploaded_at", None)
        }
        files.append(schemas.File(**file_info))

    return files  # 返回完整的文件列表，即使为空


# 文件下载
async def download_file(db: AsyncIOMotorClient, id: str):
    file = await db[FILES_COLLECTION].find_one({"_id": ObjectId(id)})
    if file:
        file["id"] = str(file.pop("_id"))
        # 仅保留需要的字段
        file_info = {
            "id": file["id"],
            "filename": file.get("filename", ""),
            "file_size": file.get("file_size", 0),
            "uploaded_at": file.get("uploaded_at", None),
            "content": file.get("content", b"")  # 假设文件内容存储在 content 字段中
        }
        return file_info
    return None


# 文件预览
async def preview_file(db: AsyncIOMotorClient, id: str):
    file = await db[FILES_COLLECTION].find_one({"_id": ObjectId(id)})
    if file:
        file["id"] = str(file.pop("_id"))
        # 仅保留需要的字段
        file_info = {
            "id": file["id"],
            "filename": file["filename"],
            "file_size": file.get("file_size", 0),
            "uploaded_at": file.get("uploaded_at", None),
            "content": file.get("content", b"")  # 假设文件内容存储在 content 字段中
        }
        return file_info
    return None


# 删除文件
async def delete_file(db: AsyncIOMotorClient, id: str):
    result = await db[FILES_COLLECTION].delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return True
    return False
