import requests

# GET 请求（无参数）
response = requests.get('http://example.com')
print(response.text)

# GET 请求（带参数）
params = {'param1': 'value1', 'param2': 'value2'}
response = requests.get('http://example.com', params=params)
print(response.text)

# POST 请求（无参数）
data = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('http://example.com', data=data)
print(response.text)

# PUT 请求（无参数）
response = requests.put('http://example.com')
print(response.text)

# DELETE 请求（无参数）
response = requests.delete('http://example.com')
print(response.text)