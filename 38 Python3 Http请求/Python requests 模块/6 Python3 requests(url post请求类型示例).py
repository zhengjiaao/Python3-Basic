import requests


# 带路径参数的 POST 请求示例
def post_with_path_param():
    user_id = '1'
    url = 'http://example.com/api/user/{}/profile'.format(user_id)
    response = requests.post(url, data={'name': 'John'})
    print(response.text)


# 带拼接参数的 POST 请求示例
def post_with_query_param():
    url = 'http://example.com/api/search'
    params = {'keyword': 'apple', 'category': 'fruit'}
    response = requests.post(url, params=params)
    print(response.text)


# 带表单参数的 POST 请求示例
def post_with_form_data():
    url = 'http://example.com/api/submit'
    data = {'username': 'john', 'password': 'secret'}
    response = requests.post(url, data=data)
    print(response.text)


# 带 JSON 参数的 POST 请求示例
def post_with_json_data():
    url = 'http://example.com/api/create'
    json_data = {'name': 'John', 'age': 30}
    response = requests.post(url, json=json_data)
    print(response.text)


# 调用示例方法
post_with_path_param()
post_with_query_param()
post_with_form_data()
post_with_json_data()
