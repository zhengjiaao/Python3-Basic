# 导入 requests 包
import requests

# 发送请求
x = requests.get('https://www.runoob.com/')

# 返回网页内容
print(x.text)
# print(x.content)  # 获取响应内容

# 返回 http 的状态码
print(x.status_code)  # 200
# 响应状态的描述
print(x.reason)  # OK
# 返回编码
print(x.apparent_encoding)  # utf-8
print(x.headers)  # 获取响应头
