# !/usr/bin/python3

import os
import shutil
import glob
import unittest


# 创建父目录
def create_parent_dir(file_path):
    parent_directory = os.path.dirname(file_path)
    if not os.path.exists(parent_directory):
        os.makedirs(parent_directory)


# 创建目录
def create_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


# 文件不存在，创建空文件
def create_empty_file(file_path):
    if not os.path.isfile(file_path):
        # 先创建父目录
        create_parent_dir(file_path)
        # 创建空文件
        open(file_path, 'w').close()


class MyTestCase(unittest.TestCase):

    def test_dir_exists(self):
        # 校验目录存在并创建父目录
        directory_path = '.path/to/directory'
        create_parent_dir(directory_path)  # 不存在父目录，则创建 '.path/to'

        # 校验文件的父目录存在并创建父目录
        file_path = '.path/to/directory/file.txt'
        create_parent_dir(file_path)  # 不存在父目录，则创建 '.path/to/directory'

        create_dir('.path/to/directory2')

    def test_dir_find(self):

        dir_path = 'path/to/directory'

        # 创建目录
        # os.mkdir('destination_folder')

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print('目录已创建')
        else:
            print('目录已存在')

        create_empty_file("path/to/directory/file.txt")
        create_empty_file("path/to/directory/sub_dir1/file1.txt")
        create_empty_file("path/to/directory/sub_dir2/file2.txt")

        # 拼接路径
        path = os.path.join('path/to/directory', 'file.txt')

        # 检查路径是否存在
        if os.path.exists(path):
            print('路径存在')
        else:
            print('路径不存在')

        # 查找所有以 .txt 结尾的文件
        files = glob.glob('path/to/directory/*.txt')

        for file in files:
            file_name = os.path.basename(file)
            print('文件名称:', file_name)

    # 列出目录中的文件和子目录：
    def test_dir_find2(self):
        dir_path = 'path/to/directory'

        items = os.listdir(dir_path)
        for item in items:
            item_path = os.path.join(dir_path, item)
            if os.path.isfile(item_path):
                print('文件:', item)
            elif os.path.isdir(item_path):
                print('目录:', item)

    # 递归列出目录中的所有文件和子目录：
    def test_dir_find3(self):
        dir_path = 'path/to/directory'

        for root, dirs, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                print('文件:', file_path)
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                print('目录:', dir_path)

    # 删除目录（包括目录中的所有文件和子目录）：
    def test_dir_delete_all(self):
        dir_path = 'path/to/directory'

        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
            print('目录已删除')
        else:
            print('目录不存在')
