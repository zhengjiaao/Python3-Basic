# main.py
from fastapi import FastAPI, HTTPException, Depends, File, UploadFile
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.responses import StreamingResponse, FileResponse
from app import crud, models, schemas
import io
import urllib.parse

from app.database import client, database
from app.models import User, UserCreate, UserBase
from app.crud import create_user, get_user, get_user_by_email, get_users, update_user, delete_user_v1, delete_user_v2

from app.routers import files, users

app = FastAPI(
    title="FastAPI MongoDB Example",
    description="An example FastAPI app with MongoDB",
    version="0.1.0",
    swagger_ui_parameters={
        "defaultModelsExpandDepth": 1,  # 默认不展开 Schemas
        "docExpansion": "none"  # 默认不展开路由
    }
)

# 包含 app/routers/*.py 中的路由
app.include_router(files.router, prefix="/api", tags=["files"])
app.include_router(users.router, prefix="/api", tags=["users"])


# Dependency
def get_db():
    return database


@app.post("/users/", response_model=User)
async def create_user_endpoint(user: UserCreate, db: AsyncIOMotorClient = Depends(get_db)):
    db_user = await get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await create_user(db, user)


@app.get("/users/", response_model=list[User])
async def read_users(skip: int = 0, limit: int = 10, db: AsyncIOMotorClient = Depends(get_db)):
    users = await get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: str, db: AsyncIOMotorClient = Depends(get_db)):
    db_user = await get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User not found")
    return db_user


@app.put("/users/{user_id}", response_model=User)
async def update_user_endpoint(user_id: str, user_update: UserBase, db: AsyncIOMotorClient = Depends(get_db)):
    db_user = await update_user(db, user_id=user_id, user_update=user_update)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User not found")
    return db_user


@app.delete("/users/delete/v1/{user_id}", response_model=bool)
async def delete_user_endpoint(user_id: str, db: AsyncIOMotorClient = Depends(get_db)):
    result = await delete_user_v1(db, user_id=user_id)
    if result is None:
        raise HTTPException(status_code=400, detail="User not found")
    return True


@app.delete("/users/delete/v2/{user_id}", response_model=User)
async def delete_user_v2_endpoint(user_id: str, db: AsyncIOMotorClient = Depends(get_db)):
    db_user = await delete_user_v2(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User not found")
    return db_user


# 文件上传
@app.post("/files/upload/", response_model=schemas.File)
async def upload_file_endpoint(file: UploadFile = File(...), db: AsyncIOMotorClient = Depends(get_db)):
    content = await file.read()
    file_upload = schemas.FileUpload(filename=file.filename, content=content)
    return await crud.upload_file(db, file_upload)


# 获取指定文件信息
@app.get("/files/{id}", response_model=schemas.File)
async def read_file_endpoint(id: str, db: AsyncIOMotorClient = Depends(get_db)):
    file = await crud.get_file(db, id)
    if file is None:
        raise HTTPException(status_code=404, detail="File not found")
    return file


# 文件列表查询
@app.get("/files/", response_model=list[schemas.File])
async def read_files_endpoint(skip: int = 0, limit: int = 10, db: AsyncIOMotorClient = Depends(get_db)):
    files = await crud.get_files(db, skip=skip, limit=limit)
    return files


# 文件下载
@app.get("/files/download/{id}")
async def download_file_endpoint(id: str, db: AsyncIOMotorClient = Depends(get_db)):
    file_info = await crud.download_file(db, id)
    if file_info is None:
        raise HTTPException(status_code=404, detail="File not found")

    # 使用 StreamingResponse 返回文件内容
    file_content = file_info.get("content", b"")
    filename = file_info.get("filename", "unknown")

    # 对文件名进行 URL 编码
    encoded_filename = urllib.parse.quote(filename)

    return StreamingResponse(
        io.BytesIO(file_content),
        media_type="application/octet-stream",
        headers={"Content-Disposition": f"attachment; filename*=UTF-8''{encoded_filename}"}
    )


# 文件预览
@app.get("/files/preview/{id}")
async def preview_file_endpoint(id: str, db: AsyncIOMotorClient = Depends(get_db)):
    file_info = await crud.preview_file(db, id)
    if file_info is None:
        raise HTTPException(status_code=404, detail="File not found")

    # 使用 StreamingResponse 返回文件内容
    file_content = file_info.get("content", b"")
    filename = file_info.get("filename", "unknown")

    # 对文件名进行 URL 编码
    encoded_filename = urllib.parse.quote(filename)

    return StreamingResponse(
        io.BytesIO(file_content),
        media_type="application/pdf",
        headers={"Content-Disposition": f"inline; filename*=UTF-8''{encoded_filename}"}
    )

    # # 使用 python-magic 确定文件的 MIME 类型，需要依赖系统安装 libmagic 组件
    # mime = magic.Magic(mime=True)
    # mime_type = mime.from_buffer(file_content)
    #
    # if mime_type:
    #     # 根据 MIME 类型决定预览或下载
    #     if mime_type.startswith("image/") or mime_type in ["application/pdf", "text/plain"]:
    #         # 支持预览的文件类型
    #         return StreamingResponse(
    #             io.BytesIO(file_content),
    #             media_type=mime_type,
    #             headers={"Content-Disposition": f"inline; filename*=UTF-8''{encoded_filename}"}
    #         )
    #     else:
    #         # 不支持预览的文件类型，触发下载
    #         return StreamingResponse(
    #             io.BytesIO(file_content),
    #             media_type="application/octet-stream",
    #             headers={"Content-Disposition": f"attachment; filename*=UTF-8''{encoded_filename}"}
    #         )
    # else:
    #     # 无法确定 MIME 类型，触发下载
    #     return StreamingResponse(
    #         io.BytesIO(file_content),
    #         media_type="application/octet-stream",
    #         headers={"Content-Disposition": f"attachment; filename*=UTF-8''{encoded_filename}"}
    #     )


# 文件删除
@app.delete("/files/delete/{id}", response_model=bool)
async def delete_file_endpoint(id: str, db: AsyncIOMotorClient = Depends(get_db)):
    file_delete = await crud.delete_file(db, id)
    if file_delete is None:
        raise HTTPException(status_code=404, detail="File not found")
    return file_delete
