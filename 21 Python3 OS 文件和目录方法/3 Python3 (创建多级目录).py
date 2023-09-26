# os.makedirs() 方法用于递归创建多层目录。
# 如果子目录创建失败或者已经存在，会抛出一个 OSError 的异常，Windows上Error 183 即为目录已经存在的异常错误。
# 如果第一个参数 path 只有一级，即只创建一层目录，则与 mkdir() 函数相同。


# !/usr/bin/python3

import os, sys

# 创建的目录
path = "./tmp/home/monthly/daily"

os.makedirs(path, 0o777)

print("路径被创建")
