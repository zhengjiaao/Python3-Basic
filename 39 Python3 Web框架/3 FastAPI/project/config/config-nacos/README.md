# FastAPI 集成 Nacos 配置管理

## 安装依赖

1. 安装依赖

首先，需要安装 fastapi、nacos-sdk-python 和其他必要的依赖。

```shell
cd fastapi-nacos
pip install -r requirements.txt
# or
pip install fastapi uvicorn nacos-sdk-python
```

2. 配置 Nacos 客户端

创建一个 Nacos 客户端来连接 Nacos 服务器并订阅配置。

3. 实现配置更新逻辑

编写一个类来管理配置，并在配置变更时更新应用中的配置。

4. 集成到 FastAPI 应用

将配置管理类集成到 FastAPI 应用中，确保在应用启动时加载配置，并在配置变更时自动更新。

## 示例代码

1. 创建 Nacos 配置管理类

```python
# config_manager.py
import nacos
from pydantic import BaseModel
from typing import Any, Dict
import json


class ConfigManager(BaseModel):
    nacos_server_addresses: str = "localhost:8848"
    data_id: str = "example-config"
    group: str = "DEFAULT_GROUP"
    _config: Dict[str, Any] = {}  # 使用下划线前缀表示这是一个内部使用的属性

    class Config:
        arbitrary_types_allowed = True  # 允许 Pydantic 模型包含任意类型的属性。

    def __init__(self, **data: Any):
        super().__init__(**data)
        self._initialize_client()  # 初始化 client 和 config_dict

    def _initialize_client(self):
        self._client = nacos.NacosClient(self.nacos_server_addresses)
        self._config_dict = {}  # 初始化 config_dict
        self._config = self._parse_config(self._client.get_config(self.data_id, self.group))
        self._client.add_config_watcher(self.data_id, self.group, self.config_callback)

    def config_callback(self, config):
        self._config = self._parse_config(config)
        print("Config updated:", self._config)

    def _parse_config(self, config: str) -> Dict[str, Any]:
        return json.loads(config)

    def get_config(self) -> Dict[str, Any]:
        return self._config

```

2. 集成到 FastAPI 应用

```python
# main.py
from fastapi import FastAPI, Depends
from app.config_manager import ConfigManager

app = FastAPI(
    title="Your API Title",
    description="Your API Description",
    version="0.1.0",
)

# config_manager = ConfigManager()

async def get_config_manager() -> ConfigManager:
    return ConfigManager()

async def startup_event():
    # 在应用启动时加载配置
    config_manager = await get_config_manager()
    config = config_manager.get_config()
    print("Initial config:", config)


async def shutdown_event():
    # 在应用关闭时执行清理操作（如果有）
    print("Application is shutting down")


app.add_event_handler("startup", startup_event)
app.add_event_handler("shutdown", shutdown_event)


@app.get("/config")
async def get_config(config_manager: ConfigManager = Depends()):
    return config_manager.get_config()


# 启动项目，或使用命令行方式：uvicorn main:apps --reload
# 访问项目-前端：http://127.0.0.1:8000/config
# 访问项目-api：http://127.0.0.1:8000/docs
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=False, workers=1)

```

3. 配置 Nacos

```python
nacos_server_addresses: str = "localhost:8848"
data_id: str = "example-config"
group: str = "DEFAULT_GROUP"
```

```json
{
  "key1": "value1",
  "key2": "value2"
}
```
