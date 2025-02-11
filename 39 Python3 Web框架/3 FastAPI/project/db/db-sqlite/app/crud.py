from sqlalchemy.orm import Session
from . import models, schemas
from math import ceil


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_users_v2(db: Session, skip: int = 0, limit: int = 10):
    total_count = db.query(models.User).count()
    total_pages = ceil(total_count / limit)
    current_page = (skip // limit) + 1
    is_first_page = current_page == 1
    is_last_page = current_page == total_pages

    users = db.query(models.User).offset(skip).limit(limit).all()

    return {
        "users": users,
        "total_count": total_count,
        "total_pages": total_pages,
        "current_page": current_page,
        "limit": limit,
        "is_first_page": is_first_page,
        "is_last_page": is_last_page
    }


def get_users_v3(db: Session, skip: int = 0, limit: int = 10):
    total_count = db.query(models.User).count()
    total_pages = ceil(total_count / limit)
    current_page = (skip // limit) + 1
    has_next_page = current_page < total_pages
    has_previous_page = current_page > 1
    next_page = current_page + 1 if has_next_page else None
    previous_page = current_page - 1 if has_previous_page else None

    users = db.query(models.User).offset(skip).limit(limit).all()

    return {
        "items": users,
        "total": total_count,
        "page": current_page,
        "size": limit,
        "pages": total_pages,
        "has_next": has_next_page,
        "has_previous": has_previous_page,
        "next_page": next_page,
        "previous_page": previous_page,
        "first_page": 1,
        "last_page": total_pages
    }


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
        email=str(user.email),  # 将 EmailStr 转换为 str
        hashed_password=fake_hashed_password,
        username=user.username
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        return None
    for var, value in vars(user_update).items():
        setattr(db_user, var, value) if value is not None else None
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        return None
    db.delete(db_user)
    db.commit()
    return db_user
