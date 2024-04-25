# 在 Python 3 中，你可以使用 urllib 或 requests 库来进行常见的 HTTP 请求操作，包括 GET、POST、PUT 和 DELETE 请求。
# 在 Python 3 中进行 GET、POST、PUT 和 DELETE 请求，包括无参数和有参数的情况：

# 以下是采用：Python 3 urllib

import urllib.request
import urllib.parse

# GET 请求（无参数）
response = urllib.request.urlopen('http://example.com')
print(response.read().decode())

# GET 请求（带参数）
params = urllib.parse.urlencode({'param1': 'value1', 'param2': 'value2'})
url = 'http://example.com/?' + params
response = urllib.request.urlopen(url)
print(response.read().decode())

# POST 请求（无参数）
data = urllib.parse.urlencode({'key1': 'value1', 'key2': 'value2'}).encode()
req = urllib.request.Request('http://example.com', data=data, method='POST')
response = urllib.request.urlopen(req)
print(response.read().decode())

# PUT 请求（无参数）
req = urllib.request.Request('http://example.com', method='PUT')
response = urllib.request.urlopen(req)
print(response.read().decode())

# DELETE 请求（无参数）
req = urllib.request.Request('http://example.com', method='DELETE')
response = urllib.request.urlopen(req)
print(response.read().decode())