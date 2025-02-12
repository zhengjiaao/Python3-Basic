# main.py
from fastapi import FastAPI, HTTPException, Depends, File, UploadFile
from pymongo import MongoClient
from fastapi.responses import StreamingResponse, FileResponse
from app import crud_files, schemas
import io
import urllib.parse

from app.database import database
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

# 包含 users.py 中的路由
app.include_router(files.router, prefix="/api", tags=["files"])
app.include_router(users.router, prefix="/api", tags=["users"])


# Dependency
def get_db():
    return database


# 文件上传
@app.post("/files/upload/", response_model=schemas.File)
async def upload_file_endpoint(file: UploadFile = File(...), db: MongoClient = Depends(get_db)):
    content = await file.read()
    file_upload = schemas.FileUpload(filename=file.filename, content=content)
    return await crud_files.upload_file(file_upload)


# 获取指定文件信息
@app.get("/files/{id}", response_model=schemas.File)
async def read_file_endpoint(id: str, db: MongoClient = Depends(get_db)):
    file = await crud_files.get_file(id)
    if file is None:
        raise HTTPException(status_code=404, detail="File not found")
    return file


# 文件下载
@app.get("/files/download/{id}")
async def download_file_endpoint(id: str, db: MongoClient = Depends(get_db)):
    file_info = await crud_files.download_file(id)
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
async def preview_file_endpoint(id: str, db: MongoClient = Depends(get_db)):
    file_info = await crud_files.preview_file(id)
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
async def delete_file_endpoint(id: str):
    file_delete = await crud_files.delete_file(id)
    if file_delete is None:
        raise HTTPException(status_code=404, detail="File not found")
    return file_delete


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=False, workers=1)
