# FastAPI 本地配置管理

## 安装依赖-前提

1. 安装依赖

首先，需要安装 fastapi和其他必要的依赖。

```shell
pip install -r requirements.txt
# or
pip install fastapi uvicorn python-dotenv pyyaml
```

## 方式一：使用环境变量

首先，安装 python-dotenv 库来加载 .env 文件中的环境变量：

```shell
pip install python-dotenv
```

然后，创建一个 .env 文件：

```text
# .env
DATABASE_URL=sqlite:///./test.db
API_KEY=your_api_key_here
```

接下来，在 FastAPI 应用中加载这些环境变量：

```python
# main.py
from fastapi import FastAPI
from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    database_url: str = os.getenv("DATABASE_URL")
    api_key: str = os.getenv("API_KEY")


settings = Settings()

app = FastAPI()


@app.get("/")
def read_root():
    return {"database_url": settings.database_url, "api_key": settings.api_key}
```

## 方式二：使用配置文件（YAML）

首先，安装 pydantic 和 pyyaml 库：

```shell
pip install pydantic pyyaml
```

然后，创建一个 config.yaml 文件：

```yaml
# config.yaml
database_url: sqlite:///./test.db
api_key: your_api_key_here
```

接下来，在 FastAPI 应用中加载这个 YAML 文件：

```python
# main.py
from fastapi import FastAPI
from pydantic import BaseSettings
import yaml


class Settings(BaseSettings):
    database_url: str
    api_key: str

    class Config:
        @classmethod
        def customise_sources(cls, init_settings, env_settings, file_secret_settings):
            return (
                init_settings,
                env_settings,
                file_secret_settings,
                cls.yaml_config_settings_source,
            )

        @classmethod
        def yaml_config_settings_source(cls, settings):
            with open("config.yaml") as f:
                return yaml.safe_load(f)


settings = Settings()

app = FastAPI()


@app.get("/")
def read_root():
    return {"database_url": settings.database_url, "api_key": settings.api_key}

```

## 方式三：使用类配置

创建一个配置类来存储配置信息：

```python
# config.py
class Config:
    database_url = "sqlite:///./test.db"
    api_key = "your_api_key_here"


class DevelopmentConfig(Config):
    debug = True


class ProductionConfig(Config):
    debug = False

```

然后，在 FastAPI 应用中使用这些配置类：

```python
# main.py
from fastapi import FastAPI
from config import DevelopmentConfig

config = DevelopmentConfig()

app = FastAPI()


@app.get("/")
def read_root():
    return {"database_url": config.database_url, "api_key": config.api_key}

```

## 方式四：使用命令行参数  argpars

使用 argparse 库来解析命令行参数：

```python
# main.py
from fastapi import FastAPI
import argparse

app = FastAPI()


def parse_arguments():
    parser = argparse.ArgumentParser(description="FastAPI Application")
    parser.add_argument("--database-url", type=str, required=True)
    parser.add_argument("--api-key", type=str, required=True)
    return parser.parse_args()


args = parse_arguments()


@app.get("/")
def read_root():
    return {"database_url": args.database_url, "api_key": args.api_key}

```

运行应用时，可以通过命令行传递参数：

```shell
python main.py --database-url sqlite:///./test.db --api-key your_api_key_here

```

## 方式五：混合配置（MixedConfig）

结合环境变量和配置文件来管理配置：

```python
# main.py
from fastapi import FastAPI
from pydantic import BaseSettings
import yaml
import os


class Settings(BaseSettings):
    database_url: str = os.getenv("DATABASE_URL")
    api_key: str = os.getenv("API_KEY")

    class Config:
        @classmethod
        def customise_sources(cls, init_settings, env_settings, file_secret_settings):
            return (
                init_settings,
                env_settings,
                file_secret_settings,
                cls.yaml_config_settings_source,
            )

        @classmethod
        def yaml_config_settings_source(cls, settings):
            with open("config.yaml") as f:
                return yaml.safe_load(f)


settings = Settings()

app = FastAPI()


@app.get("/")
def read_root():
    return {"database_url": settings.database_url, "api_key": settings.api_key}

```

通过这些示例，你可以根据项目需求选择合适的方式来管理本地配置。
