#!/usr/bin/python3

import json

# Python 字典类型转换为 JSON 对象
data1 = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data1)
print("Python 原始数据：", repr(data1))
print("JSON 对象：", json_str)

# 写入 JSON 数据
with open('data.json', 'w') as f:
    json.dump(json_str, f)

# 读取数据
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)