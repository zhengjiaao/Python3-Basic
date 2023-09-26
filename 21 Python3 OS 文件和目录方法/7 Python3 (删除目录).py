# os.rmdir() 方法用于删除指定路径的目录。仅当这文件夹是空的才可以, 否则, 抛出OSError。

# !/usr/bin/python3

import os, sys

# 列出目录
print("目录为: %s" % os.listdir(os.getcwd()))

# 删除路径
os.rmdir("mydir")

# 列出重命名后的目录
print("目录为: %s" % os.listdir(os.getcwd()))
