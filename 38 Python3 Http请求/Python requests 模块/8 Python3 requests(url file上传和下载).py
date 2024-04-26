import requests
import json
import os
import unittest


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

        # 打开文件
        with open(file_path, 'rb') as file:
            file_data = file.read()

        # 发送请求
        response = requests.post(url, files={'file': file_data})

        print(response.text)

    # 上传多文件(无参数)
    def test_upload_file_request2(self):
        # 上传文件-多个
        url = 'http://localhost:19000/post/upload/v2'
        file_paths = ['tmp/myfile.txt', 'tmp/myfile2.txt']
        # 构建文件列表
        files = []
        for file_path in file_paths:
            with open(file_path, 'rb') as file:
                file_data = file.read()
            # 添加文件
            file_name = file_path.split('/')[-1]
            files.append(('files', (file_name, file_data)))

        # 发送请求
        response = requests.post(url, files=files)

        print(response.text)

    # 上传单文件(携带拼接参数)
    def test_upload_files_request3(self):
        url = 'http://localhost:19000/post/upload/v3'
        file_path = 'tmp/myfile.txt'

        # 构建参数
        params = {'filename': 'myfile-new.txt'}

        # 打开文件
        with open(file_path, 'rb') as file:
            file_data = file.read()

        # 发送请求
        response = requests.post(url, files={'file': file_data}, data=params)

        print(response.text)

    # 上传多文件(携带拼接参数)
    def test_upload_files_request4(self):
        # 上传文件并携带参数
        url = 'http://localhost:19000/post/upload/v5'

        # 文件路径
        file_paths = ['tmp/myfile.txt', 'tmp/myfile2.txt']

        # 构建参数
        params = {'filename': 'myfile-new.txt'}

        # 构建文件列表
        files = []
        for file_path in file_paths:
            with open(file_path, 'rb') as file:
                file_data = file.read()

            # 添加文件
            file_name = file_path.split('/')[-1]
            files.append(('files', (file_name, file_data)))

        # 发送请求
        response = requests.post(url, files=files, data=params)

        print(response.text)
