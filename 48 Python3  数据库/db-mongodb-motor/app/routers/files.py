# app/routers/files.py
from fastapi import UploadFile, APIRouter, Depends, File, HTTPException
from fastapi.responses import StreamingResponse, FileResponse
from .. import crud, schemas
import io
import urllib.parse

from motor.motor_asyncio import AsyncIOMotorClient
from .. import database

router = APIRouter()


def get_db():
    return database.database


# 文件上传
@router.post("/files/upload/", response_model=schemas.File)
async def upload_file_endpoint(file: UploadFile = File(...), db: AsyncIOMotorClient = Depends(get_db)):
    content = await file.read()
    file_upload = schemas.FileUpload(filename=file.filename, content=content)
    return await crud.upload_file(db, file_upload)


# 获取指定文件信息
@router.get("/files/{id}", response_model=schemas.File)
async def read_file_endpoint(id: str, db: AsyncIOMotorClient = Depends(get_db)):
    file = await crud.get_file(db, id)
    if file is None:
        raise HTTPException(status_code=404, detail="File not found")
    return file


# 文件列表查询
@router.get("/files/", response_model=list[schemas.File])
async def read_files_endpoint(skip: int = 0, limit: int = 10, db: AsyncIOMotorClient = Depends(get_db)):
    files = await crud.get_files(db, skip=skip, limit=limit)
    return files


# 文件下载
@router.get("/files/download/{id}")
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
@router.get("/files/preview/{id}")
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
@router.delete("/files/delete/{id}", response_model=bool)
async def delete_file_endpoint(id: str, db: AsyncIOMotorClient = Depends(get_db)):
    file_delete = await crud.delete_file(db, id)
    if file_delete is None:
        raise HTTPException(status_code=404, detail="File not found")
    return file_delete
