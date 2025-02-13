# apps/routers/files.py
import os
import urllib.parse
import mimetypes

from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, Response
from sqlalchemy.orm import Session
from ..core import crud_files, schemas, database

files_api = APIRouter()


async def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@files_api.post("/files/", response_model=schemas.File)
async def create_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_data = await file.read()
    file_create = schemas.FileCreate(filename=file.filename)
    return await crud_files.create_file(db=db, file=file_create, file_data=file_data)


@files_api.get("/files/{file_id}", response_model=schemas.File)
async def read_file(file_id: str, db: Session = Depends(get_db)):
    db_file = await crud_files.get_file(db, file_id=file_id)
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found")
    return db_file


@files_api.get("/files/", response_model=list[schemas.File])
async def read_files(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    files = await crud_files.get_files(db, skip=skip, limit=limit)
    return files


@files_api.get("/files/{file_id}/download")
async def download_file(file_id: str, db: Session = Depends(get_db)):
    db_file = await crud_files.get_file(db, file_id=file_id)
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found")
    file_path = os.path.join("uploads", db_file.file_id)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found on server")

    # 使用 urllib.parse.quote 对文件名进行编码
    encoded_filename = urllib.parse.quote(db_file.filename)
    headers = {"Content-Disposition": f"attachment; filename*=UTF-8''{encoded_filename}"}

    return Response(content=open(file_path, "rb").read(), media_type="application/octet-stream", headers=headers)


@files_api.delete("/files/{file_id}", response_model=schemas.File)
async def delete_file(file_id: str, db: Session = Depends(get_db)):
    db_file = await crud_files.get_file(db, file_id=file_id)
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found")
    await crud_files.delete_file(db, file_id=file_id)
    return db_file


@files_api.get("/files/{file_id}/preview")
async def preview_file(file_id: str, db: Session = Depends(get_db)):
    db_file = await crud_files.get_file(db, file_id=file_id)
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found")
    file_path = os.path.join("uploads", db_file.file_id)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found on server")

    # 获取文件的 MIME 类型
    mime_type, _ = mimetypes.guess_type(db_file.filename)
    if not mime_type:
        mime_type = "application/octet-stream"

    # 支持预览的 MIME 类型列表
    previewable_mime_types = ["application/pdf", "text/plain", "image/jpeg", "image/png", "image/gif"]

    if mime_type in previewable_mime_types:
        disposition = "inline"
    else:
        disposition = "attachment"

    # 使用 urllib.parse.quote 对文件名进行编码
    encoded_filename = urllib.parse.quote(db_file.filename)
    headers = {"Content-Disposition": f"{disposition}; filename*=UTF-8''{encoded_filename}"}

    return Response(content=open(file_path, "rb").read(), media_type=mime_type, headers=headers)
