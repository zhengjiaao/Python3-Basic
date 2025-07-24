# app/config.py
from pydantic_settings import BaseSettings
from pydantic import ConfigDict
import os

# 获取当前文件所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

class Settings(BaseSettings):
    database_url: str
    api_key: str

    print(current_dir)
    print(os.path.join(current_dir, '../.env'))

    # 指定 .env 文件路径
    model_config = ConfigDict(env_file=os.path.join(current_dir, '../.env'), env_file_encoding='utf-8')


# 实例化配置对象
settings = Settings()

# 可选：调试输出配置信息
if __name__ == "__main__":
    print(settings.model_dump())
