# os.pardir() 获取当前目录的父目录（上一级目录），以字符串形式显示目录名。

import os

# 当前工作目录
path = os.getcwd()
print("当前工作目录: ", path)

# 父目录
parent = os.path.join(path, os.pardir)

# 父目录
print("\n父目录:", os.path.abspath(parent))
