# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

# 创建配置类
class Settings(BaseModel):
    database_url: str = os.getenv("DATABASE_URL")
    api_key: str = os.getenv("api_key")

# 创建配置对象
settings = Settings()

# 创建FastAPI应用
app = FastAPI()

@app.get("/")
def read_root():
    return {"database_url": settings.database_url, "api_key": settings.api_key}