from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine
from app.routers import users

models.Base.metadata.create_all(bind=engine)

# app = FastAPI()

app = FastAPI(
    title="Your API Title",
    description="Your API Description",
    version="0.1.0",
    swagger_ui_parameters={
        "defaultModelsExpandDepth": 1,  # 默认不展开 Schemas
        "docExpansion": "none"  # 默认不展开路由
    }
)

# 包含 users.py 中的路由
app.include_router(users.router, prefix="/api", tags=["users"])


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=str(user.email))
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/v2", response_model=schemas.PaginatedUsers)
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    paginated_users = crud.get_users_v2(db, skip=skip, limit=limit)
    return paginated_users


@app.get("/users/v3", response_model=schemas.PaginatedResponse[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    paginated_users = crud.get_users_v3(db, skip=skip, limit=limit)
    return paginated_users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.update_user(db, user_id=user_id, user_update=user_update)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

