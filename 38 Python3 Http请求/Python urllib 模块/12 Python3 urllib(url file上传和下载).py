import urllib.request
import urllib.parse
import mimetypes
import json
import unittest
import os


# Python3 Python urllib 模块 file文件上传、下载实例 单元测试
class MyTestCase(unittest.TestCase):

    # 在每个测试方法之前执行的操作
    def setUp(self):
        parent_directory = 'tmp'
        if not os.path.exists(parent_directory):
            os.makedirs(parent_directory)

    # =================创建文件
    def test_write_file_request1(self):

        # 写入文件
        file_path = 'tmp/myfile.txt'

        file_path2 = 'tmp/myfile2.txt'

        with open(file_path, 'w') as file:
            file.write('Hello, World!')

        with open(file_path2, 'w') as file:
            file.write('Hello, World2!')

    # =================上传文件

    # 上传单文件(无参数)
    def test_upload_file_request1(self):
        # 上传文件
        url = 'http://localhost:19000/post/upload/v1'
        file_path = 'tmp/myfile.txt'

        # 构建请求体数据
        boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
        data = '--' + boundary + '\r\n' + \
               'Content-Disposition: form-data; name="file"; filename="file.txt"\r\n' + \
               'Content-Type: application/octet-stream\r\n\r\n'

        with open(file_path, 'rb') as file:
            file_data = file.read()

        end_data = '\r\n--' + boundary + '--\r\n'

        # 构建请求对象
        request_data = data.encode('utf-8') + file_data + end_data.encode('utf-8')
        request = urllib.request.Request(url, data=request_data)
        request.add_header('Content-Type', 'multipart/form-data; boundary=' + boundary)

        # 发送请求
        response = urllib.request.urlopen(request)

        print(response.read().decode())

    # 上传多文件(无参数)
    def test_upload_file_request2(self):
        # 上传文件-多个
        url = 'http://localhost:19000/post/upload/v2'
        file_paths = ['tmp/myfile.txt', 'tmp/myfile2.txt']

        # 构建请求体数据
        boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
        data = []

        for file_path in file_paths:
            file_data = open(file_path, 'rb').read()

            # 添加文件
            file_name = file_path.split('/')[-1]
            data.append(b'--' + boundary.encode('utf-8'))
            data.append(
                'Content-Disposition: form-data; name="files"; filename="{}"'.format(file_name).encode('utf-8'))
            data.append(b'Content-Type: application/octet-stream')
            data.append(b'')
            data.append(file_data)

        data.append(b'--' + boundary.encode('utf-8') + b'--')
        data.append(b'')

        # 构建请求对象
        request_data = b'\r\n'.join(data)
        request = urllib.request.Request(url, data=request_data)
        request.add_header('Content-Type', 'multipart/form-data; boundary=' + boundary)

        # 发送请求
        response = urllib.request.urlopen(request)

        print(response.read().decode())

    # 上传单文件(携带拼接参数)
    def test_upload_files_request3(self):
        url = 'http://localhost:19000/post/upload/v3'
        file_path = 'tmp/myfile.txt'

        # 构建参数
        params = {'filename': 'myfile-new.txt'}

        # 构建文件数据
        file_data = open(file_path, 'rb').read()

        # 构建请求体数据
        boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
        data = []

        # 添加参数
        for key, value in params.items():
            data.append(b'--' + boundary.encode('utf-8'))
            data.append('Content-Disposition: form-data; name="{}"'.format(key).encode('utf-8'))
            data.append(b'')
            data.append(value.encode('utf-8'))

        # 添加文件
        file_name = file_path.split('/')[-1]
        mimetype, _ = mimetypes.guess_type(file_path)
        data.append(b'--' + boundary.encode('utf-8'))
        data.append('Content-Disposition: form-data; name="file"; filename="{}"'.format(file_name).encode('utf-8'))
        data.append('Content-Type: {}'.format(mimetype).encode('utf-8'))
        data.append(b'')
        data.append(file_data)

        data.append(b'--' + boundary.encode('utf-8') + b'--')
        data.append(b'')

        # 构建请求对象
        request_data = b'\r\n'.join(data)
        request = urllib.request.Request(url, data=request_data)
        request.add_header('Content-Type', 'multipart/form-data; boundary=' + boundary)

        # 发送请求
        response = urllib.request.urlopen(request)

        print(response.read().decode())

    # 上传多文件(携带拼接参数)
    def test_upload_files_request4(self):
        # 上传文件并携带参数
        url = 'http://localhost:19000/post/upload/v5'

        # 文件路径
        file_paths = ['tmp/myfile.txt', 'tmp/myfile2.txt']

        # 构建参数
        params = {'filename': 'myfile-new.txt'}

        # 构建请求体数据
        boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW'
        data = []

        # 添加参数
        for key, value in params.items():
            data.append(b'--' + boundary.encode('utf-8'))
            data.append('Content-Disposition: form-data; name="{}"'.format(key).encode('utf-8'))
            data.append(b'')
            data.append(value.encode('utf-8'))

        # 添加文件
        for file_path in file_paths:
            file_data = open(file_path, 'rb').read()

            # 添加文件
            file_name = file_path.split('/')[-1]
            data.append(b'--' + boundary.encode('utf-8'))
            data.append(
                'Content-Disposition: form-data; name="files"; filename="{}"'.format(file_name).encode('utf-8'))
            data.append(b'Content-Type: application/octet-stream')
            data.append(b'')
            data.append(file_data)

        data.append(b'--' + boundary.encode('utf-8') + b'--')
        data.append(b'')

        # 构建请求对象
        request_data = b'\r\n'.join(data)
        request = urllib.request.Request(url, data=request_data)
        request.add_header('Content-Type', 'multipart/form-data; boundary=' + boundary)

        # 发送请求
        response = urllib.request.urlopen(request)

        print(response.read().decode())

    # =================下载文件===============

    # get 根据url下载
    def test_downloaded_file_request1(self):
        # 1.先获取文件url
        params = urllib.parse.urlencode({'filename': 'jpg.jpg'})
        url = 'http://localhost:19000/get/download/v1?' + params
        response = urllib.request.urlopen(url)
        result_file_url = response.read().decode()
        print(result_file_url)

        # 2.根据文件url下载
        file_path = 'tmp/downloaded_file.jpg'

        with urllib.request.urlopen(result_file_url) as response:
            with open(file_path, 'wb') as file:
                file.write(response.read())

    # get 下载文件流
    def test_downloaded_file_request2(self):
        # 根据文件url下载
        file_url = 'http://localhost:19000/get/download/v2?filename=jpg.jpg'
        file_path = 'tmp/downloaded_file2.jpg'

        with urllib.request.urlopen(file_url) as response:
            with open(file_path, 'wb') as file:
                file.write(response.read())

    # post 下载文件流
    def test_downloaded_file_request3(self):
        # 根据文件url下载
        file_url = 'http://localhost:19000/post/download/v1?filename=jpg.jpg'
        file_path = 'tmp/downloaded_file3.jpg'
        data = b''  # data 参数设置为空字节流

        # 构建请求数据
        # params = {'param1': 'value1', 'param2': 'value2'}
        # data = urllib.parse.urlencode(params).encode('utf-8')

        # 构建请求对象
        request = urllib.request.Request(file_url, data=data, method='POST')

        # 发送请求
        response = urllib.request.urlopen(request)

        # 读取文件流
        file_data = response.read()

        # 保存文件
        with open(file_path, 'wb') as file:
            file.write(file_data)

if __name__ == '__main__':
    unittest.main()
