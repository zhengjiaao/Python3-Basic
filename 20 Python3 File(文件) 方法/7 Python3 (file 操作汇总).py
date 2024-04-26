import os
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


class MyTestCase(unittest.TestCase):

    # 在每个测试方法之前执行的操作
    # 创建测试的父目录
    def setUp(self):

        parent_directory = 'tmp'
        if not os.path.exists(parent_directory):
            os.makedirs(parent_directory)

        create_dir('path/to')

    def test_file_find(self):
        file_path = 'path/to/file.txt'

        # 创建文件父目录
        create_parent_dir(file_path)

        # 校验文件存在，不存在，则创建文件
        if os.path.isfile(file_path):
            print('文件存在')
        else:
            print('文件不存在')
            # 文件不存在，创建文件
            with open(file_path, 'w') as file:
                file.write('Hello, World!')

        # 获取文件名称
        file_name = os.path.basename(file_path)
        print('文件名称:', file_name)

        # 获取文件绝对路径
        absolute_path = os.path.abspath(file_path)
        print('文件绝对路径:', absolute_path)

        # 获取文件相对路径
        relative_path = os.path.relpath(file_path)
        print('文件相对路径:', relative_path)

        # 获取文件父路径
        parent_path = os.path.dirname(file_path)
        print('文件父路径:', parent_path)

        # 检查路径是否存在
        exists = os.path.exists(file_path)
        print(exists)

        # 获取文件大小
        size = os.path.getsize(file_path)
        print(size)

        # 获取文件的最后修改时间
        modification_time = os.path.getmtime(file_path)
        print(modification_time)

        # 删除文件
        if os.path.isfile(file_path):
            os.remove(file_path)
            print('文件已删除')
        else:
            print('文件不存在')

    # 校验文件是否存在，并在文件不存在时创建一个空文件。
    def test_file_exists(self):
        file_path = 'path/to/file.txt'

        # 检查文件是否存在
        if not os.path.isfile(file_path):
            # 文件不存在，创建空文件
            open(file_path, 'w').close()
            print('已创建空文件：', file_path)
        else:
            print('文件已存在：', file_path)

    # 创建一个文件，并写入内容
    def test_write_file1(self):
        file_path = 'path/to/file1.txt'
        with open(file_path, 'w') as file:
            file.write('Hello, World!')

    # 创建一个文件，并写入内容
    def test_write_file2(self):
        file_path = 'path/to/file2.txt'
        f = open(file_path, "w")
        f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
        # 关闭打开的文件
        f.close()

    # 读取文件内容
    def test_read_file1(self):
        file_path = 'path/to/file1.txt'
        with open(file_path, 'rb') as file:
            file_data = file.read()
        print(file_data)

    # 读取文件内容
    def test_read_file2(self):
        file_path = 'path/to/file2.txt'
        # 打开一个文件
        f = open(file_path, "r")
        str = f.read()
        print(str)
        # 关闭打开的文件
        f.close()

    # 创建文件父目录
    def test_create_parent_dir(self):
        file_path = 'path/to/parentdir/file2.txt'
        create_parent_dir(file_path)

    # 复制文件
    def test_copy_file1(self):
        file_path = 'path/to/file1.txt'

    # 移动文件
    def test_move_file2(self):
        src = 'path/to/file1.txt'
        dst = 'path/to/move/new_file.txt'

        create_parent_dir(dst)

        # 移动文件
        os.replace(src, dst)

    # 重命名文件
    def test_rename_file(self):
        src = 'path/to/file1.txt'
        dst = 'path/to/new_name.txt'
        # 重命名文件
        os.rename(src, dst)


if __name__ == '__main__':
    unittest.main()
