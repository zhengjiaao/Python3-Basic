#!/usr/bin/python3

# os.remove() 方法用于删除指定路径的文件。如果指定的路径是一个目录，将抛出OSError。
# 在Unix, Windows中有效

import os, sys

# 列出目录
print("目录为: %s" % os.listdir(os.getcwd()))

# 移除
os.remove("aa.txt")

# 移除后列出目录
print("移除后 : %s" % os.listdir(os.getcwd()))
