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

# 输出结果

# Python 原始数据： {'no': 1, 'name': 'Runoob', 'url': 'http://www.runoob.com'}
# JSON 对象： {"no": 1, "name": "Runoob", "url": "http://www.runoob.com"}

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print("data2['name']: ", data2['name'])
print("data2['url']: ", data2['url'])

# 输出结果

# data2['name']:  Runoob
# data2['url']:  http://www.runoob.com
