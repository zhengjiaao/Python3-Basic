# !/usr/bin/python3

import os
import shutil
import glob

# 创建目录
os.mkdir('my_directory')

# 拼接路径
path = os.path.join('my_directory', 'my_file.txt')

# 检查路径是否存在
if os.path.exists(path):
    print('路径存在')
else:
    print('路径不存在')

# 写入文件
with open('my_directory/my_file.txt', 'w') as file:
    file.write('Hello, World!')

# 读取文件内容
with open('my_directory/my_file.txt', 'r') as file:
    content = file.read()
    print(content)

# 查找所有以 .txt 结尾的文件
files = glob.glob('my_directory/*.txt')

# 创建目录
os.mkdir('destination_folder')

# 复制文件
shutil.copy('my_directory/my_file.txt', 'destination_folder/')
# shutil.copy('my_directory/my_file.txt', 'destination_folder/my_file.txt')

# 删除文件
os.remove('my_directory/my_file.txt')

