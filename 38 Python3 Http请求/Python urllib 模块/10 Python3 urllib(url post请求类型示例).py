import urllib.request
import urllib.parse
import json

# 路径参数
url = 'http://example.com/path/123'
data = b''  # data 参数设置为空字节流

req = urllib.request.Request(url, data=data, method='POST')
with urllib.request.urlopen(req) as response:
    print(response.read().decode())

# 拼接参数
base_url = 'http://example.com/api'
params = {'param1': 'value1', 'param2': 'value2'}
encoded_params = urllib.parse.urlencode(params).encode('utf-8')

url = base_url + '?' + encoded_params
data = b''

req = urllib.request.Request(url, data=data, method='POST')
with urllib.request.urlopen(req) as response:
    print(response.read().decode())

# 表单参数
url = 'http://example.com/api'
form_data = {'key1': 'value1', 'key2': 'value2'}
encoded_data = urllib.parse.urlencode(form_data).encode('utf-8')

req = urllib.request.Request(url, data=encoded_data, method='POST')
req.add_header('Content-Type', 'application/x-www-form-urlencoded')

with urllib.request.urlopen(req) as response:
    print(response.read().decode())

# JSON 参数
url = 'http://example.com/api'
json_data = {'key1': 'value1', 'key2': 'value2'}
encoded_data = json.dumps(json_data).encode('utf-8')

req = urllib.request.Request(url, data=encoded_data, method='POST')
req.add_header('Content-Type', 'application/json')

with urllib.request.urlopen(req) as response:
    print(response.read().decode())
