# app/crud_files.py
from gridfs import GridFS
from datetime import datetime, timezone
# from schemas import FileUpload, File # 使用绝对路径，不同级目录下
from . import schemas  # 使用相对导入,同级目录下
from bson.objectid import ObjectId
from . import database


def get_db():
    return database.database


def get_gridfs():
    return GridFS(get_db())


async def upload_file(file: schemas.FileUpload):
    # 使用 GridFS 存储文件内容
    fs = get_gridfs()
    file_id = fs.put(file.content, filename=file.filename, uploaded_at=datetime.now(timezone.utc),
                     file_size=len(file.content))

    # 获取文件信息
    grid_out = fs.get(file_id)
    file_info = {
        "id": str(grid_out._id),
        "filename": grid_out.filename,
        "file_size": grid_out.file_size,
        "uploaded_at": grid_out.uploaded_at
    }
    return schemas.File(**file_info)


async def get_file(id: str):
    fs = get_gridfs()
    file_id = ObjectId(id)
    try:
        grid_out = fs.get(file_id)
        file_info = {
            "id": str(grid_out._id),
            "filename": grid_out.filename,
            "file_size": grid_out.file_size,
            "uploaded_at": grid_out.uploaded_at
        }
        return schemas.File(**file_info)
    except Exception as e:
        return None


async def download_file(id: str):
    fs = get_gridfs()
    file_id = ObjectId(id)
    try:
        grid_out = fs.get(file_id)
        file_info = {
            "content": grid_out.read(),
            "filename": grid_out.filename,
            "file_size": grid_out.file_size,
            "uploaded_at": grid_out.uploaded_at
        }
        return file_info
    except Exception as e:
        return None


async def preview_file(id: str):
    fs = get_gridfs()
    file_id = ObjectId(id)
    try:
        grid_out = fs.get(file_id)
        file_info = {
            "content": grid_out.read(),
            "filename": grid_out.filename,
            "file_size": grid_out.file_size,
            "uploaded_at": grid_out.uploaded_at
        }
        return file_info
    except Exception as e:
        return None


async def delete_file(id: str):
    fs = get_gridfs()
    file_id = ObjectId(id)
    try:
        fs.delete(file_id)
        return True
    except Exception as e:
        return False
