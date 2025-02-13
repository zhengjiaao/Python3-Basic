from fastapi import FastAPI
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
import yaml
import os


# 混合配置：先从 .env 文件中读取环境变量，再从 YAML 文件中读取配置，如果 YAML 文件不存在则使用默认配置。

# 定义配置类
class Settings(BaseSettings):
    database_url: str = Field(..., env="DATABASE_URL")
    api_key: str = Field(..., env="API_KEY")

    model_config = SettingsConfigDict(
        env_file=".env",  # 从 .env 文件中读取环境变量
        env_file_encoding="utf-8",
    )

    def __init__(self, **data):
        super().__init__(**data)
        # 读取 YAML 文件内容并更新配置
        config_file_path = os.path.join(os.path.dirname(__file__), "config.yaml")
        print(f"Attempting to read config from {config_file_path}")
        if os.path.exists(config_file_path):
            with open(config_file_path, "r") as f:
                config_data = yaml.safe_load(f) or {}
                print("Config data:", config_data)
                for key, value in config_data.items():
                    if hasattr(self, key):
                        setattr(self, key, value)


# 创建 settings 实例
settings = Settings()

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
