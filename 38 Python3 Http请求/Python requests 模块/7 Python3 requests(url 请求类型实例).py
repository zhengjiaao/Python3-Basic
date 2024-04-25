import requests
import json
import unittest


# Python3 Python urllib 模块 get、post请求类型实例 单元测试
class MyTestCase(unittest.TestCase):

    # =================get 请求实例
    def test_get_request(self):
        # get 无参,返回字符串
        response = requests.get('http://localhost:19000/get')
        print(response.text)

        # get 有参,返回字符串
        params = {'param': 'value1'}
        response = requests.get('http://localhost:19000/get/param/v1', params=params)
        print(response.text)

        # get 无参，返回json数据结构
        response = requests.get('http://localhost:19000/get/object/v1')
        json_data = response.json()

        # 对返回的 JSON 数据进行处理
        self.assertEqual(json_data['id'], '1')
        print(json_data['id'])
        print(json_data['name'])
        print(json_data['date'])

    # =================post 请求实例
    def test_post_request(self):
        # post 无参,返回字符串
        response = requests.post('http://localhost:19000/post')
        print(response.text)

        # post 拼接参数,返回字符串
        url = 'http://localhost:19000/post/param'
        params = {'name': '李四', 'age': 18}
        response = requests.post(url, params=params)
        print(response.text)

        # post JSON 参数，返回json
        url = 'http://localhost:19000/post/object/v2'
        json_data = {'id': '1', 'name': '李四', 'date': '2024-04-25T08:56:07.694+00:00'}
        response = requests.post(url, json=json_data)
        print(response.text)
        print(response.json())
        # 对返回的 JSON 数据进行处理
        json_data = response.json()
        print(json_data['id'])
        print(json_data['name'])
        print(json_data['date'])


if __name__ == '__main__':
    unittest.main()
