# app/routers/files.py
from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database

router = APIRouter()


async def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        await db.close()


@router.post("/files/", response_model=schemas.File)
async def create_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_data = await file.read()
    file_create = schemas.FileCreate(filename=file.filename, data=file_data)
    return await crud.create_file(db=db, file=file_create)


@router.get("/files/{file_id}", response_model=schemas.File)
async def read_file(file_id: int, db: Session = Depends(get_db)):
    db_file = await crud.get_file(db, file_id=file_id)
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found")
    return db_file


@router.get("/files/", response_model=list[schemas.File])
async def read_files(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    files = await crud.get_files(db, skip=skip, limit=limit)
    return files
