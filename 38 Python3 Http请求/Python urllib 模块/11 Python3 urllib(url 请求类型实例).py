import urllib.request
import urllib.parse
import json
import unittest


# Python3 Python urllib 模块 get、post请求类型实例 单元测试
class MyTestCase(unittest.TestCase):

    # =================get 请求实例
    def test_get_request(self):
        # get 无参,返回字符串
        response = urllib.request.urlopen('http://localhost:19000/get')
        result = response.read().decode()
        print(result)
        # self.assertEqual(result, 'Expected response')

    def test_get_request2(self):
        # get 有参,返回字符串
        params = urllib.parse.urlencode({'param': 'value1'})
        url = 'http://localhost:19000/get/param/v1?' + params
        response = urllib.request.urlopen(url)
        print(response.read().decode())

    def test_get_request3(self):
        # get 无参，返回json数据结构
        response = urllib.request.urlopen('http://localhost:19000/get/object/v1')
        result = response.read().decode()
        print(result)
        json_data = json.loads(result)  # 解析 JSON 数据
        # 对解析后的 JSON 数据进行断言或其他处理
        self.assertEqual(json_data['id'], '1')
        # 将 JSON 对象转换为 Python 字典
        data_dic = json.loads(result)
        print("data_dic['id']: ", data_dic['id'])
        print("data_dic['name']: ", data_dic['name'])
        print("data_dic['date']: ", data_dic['date'])

    # =================post 请求实例

    def test_post_request(self):
        # post 无参,返回字符串
        url = 'http://localhost:19000/post'
        data = b''  # data 参数设置为空字节流

        req = urllib.request.Request(url, data=data, method='POST')
        with urllib.request.urlopen(req) as response:
            print(response.read().decode())

    def test_post_request2(self):
        # post 拼接参数,返回字符串
        params = urllib.parse.urlencode({'name': '李四', 'age': 18})
        url = 'http://localhost:19000/post/param?' + params

        data = b''

        req = urllib.request.Request(url, data=data, method='POST')
        with urllib.request.urlopen(req) as response:
            print(response.read().decode())

    def test_post_request3(self):
        # post JSON 参数，返回json
        url = 'http://localhost:19000/post/object/v2'
        json_data = {'id': '1', 'name': '李四', 'date': '2024-04-25T08:56:07.694+00:00'}
        encoded_data = json.dumps(json_data).encode('utf-8')

        req = urllib.request.Request(url, data=encoded_data, method='POST')
        req.add_header('Content-Type', 'application/json')

        with urllib.request.urlopen(req) as response:
            result = response.read().decode()
            print(result)
            # 将 JSON 对象转换为 Python 字典
            data_dic = json.loads(result)
            print("data_dic['id']: ", data_dic['id'])
            print("data_dic['name']: ", data_dic['name'])
            print("data_dic['date']: ", data_dic['date'])


if __name__ == '__main__':
    unittest.main()
