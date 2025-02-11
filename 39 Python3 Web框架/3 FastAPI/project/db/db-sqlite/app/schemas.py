from pydantic import BaseModel, EmailStr, Field
from typing import List, TypeVar, Generic

T = TypeVar('T')


class UserBase(BaseModel):
    email: EmailStr
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class UserUpdate(UserBase):
    email: EmailStr | None = None
    username: str | None = None
    password: str | None = None


class PaginatedUsers(BaseModel):
    users: List[User]
    total_count: int
    total_pages: int
    current_page: int
    limit: int
    is_first_page: bool
    is_last_page: bool


# 通用的分页模型-无swagger描述
# class PaginatedResponse(BaseModel, Generic[T]):
#     items: List[T]
#     total: int
#     page: int
#     size: int
#     pages: int
#     has_next: bool
#     has_previous: bool
#     next_page: int | None = None
#     previous_page: int | None = None
#     first_page: int
#     last_page: int


# 通用的分页模型-带swagger描述
class PaginatedResponse(BaseModel, Generic[T]):
    items: List[T] = Field(
        ...,
        description="列表中的项目。"
    )
    total: int = Field(
        ...,
        description="总项目数。"
    )
    page: int = Field(
        ...,
        description="当前页码。"
    )
    size: int = Field(
        ...,
        description="每页的项目数。"
    )
    pages: int = Field(
        ...,
        description="总页数。"
    )
    has_next: bool = Field(
        ...,
        description="是否存在下一页。"
    )
    has_previous: bool = Field(
        ...,
        description="是否存在上一页。"
    )
    next_page: int | None = Field(
        None,
        description="下一页的页码，如果没有下一页则为 `null`。"
    )
    previous_page: int | None = Field(
        None,
        description="上一页的页码，如果没有上一页则为 `null`。"
    )
    first_page: int = Field(
        ...,
        description="第一页的页码。"
    )
    last_page: int = Field(
        ...,
        description="最后一页的页码。"
    )
