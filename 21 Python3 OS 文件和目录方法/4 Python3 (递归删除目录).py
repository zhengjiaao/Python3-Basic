# os.removedirs() 方法用于递归删除目录。像rmdir(), 如果子文件夹成功删除, removedirs()才尝试它们的父文件夹,直到抛出一个error(它基本上被忽略,因为它一般意味着你文件夹不为空)。

# !/usr/bin/python3

import os, sys

# 列出目录
print("目录为: %s" % os.listdir(os.getcwd()))

# 移除
os.removedirs("test")

# 列出移除后的目录
print("移除后目录为:" % os.listdir(os.getcwd()))
