# 使用 json.dumps 与 json.loads 实例

# !/usr/bin/python3

import json

# Python 字典类型转换为 JSON 对象
data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data)
print("Python 原始数据：", repr(data))
print("JSON 对象：", json_str)

# 结果输出

# Python 原始数据： {'no': 1, 'name': 'Runoob', 'url': 'http://www.runoob.com'}
# JSON 对象： {"no": 1, "name": "Runoob", "url": "http://www.runoob.com"}
