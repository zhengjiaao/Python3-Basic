from fastapi import FastAPI
from pydantic import Field
from pydantic_settings import BaseSettings  # 使用 BaseSettings 支持环境变量和文件配置
import yaml
import os

# 定义配置类
class Settings(BaseSettings):
    database_url: str = Field(..., env="DATABASE_URL")
    api_key: str = Field(..., env="API_KEY")

# 读取配置文件内容
config_file_path = os.path.join(os.path.dirname(__file__), "config.yaml")
print(f"Attempting to read config from {config_file_path}")
with open(config_file_path, "r") as f:
    config_data = yaml.safe_load(f) or {}
    print("Config data:", config_data)

# 将 config_data 解析给 settings 类
settings = Settings(**config_data)

app = FastAPI()

@app.get("/")
def read_root():
    return {"database_url": settings.database_url, "api_key": settings.api_key}

# 启动项目，或使用命令行方式：uvicorn main:apps --reload
# 访问项目-前端：http://127.0.0.1:8000/
# 访问项目-api：http://127.0.0.1:8000/docs
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=False, workers=1)
