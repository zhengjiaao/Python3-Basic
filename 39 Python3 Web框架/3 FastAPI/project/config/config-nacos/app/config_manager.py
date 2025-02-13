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