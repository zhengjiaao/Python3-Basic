#!/usr/bin/python3

import os, sys

# os.chdir() 方法用于改变当前工作目录到指定的路径

path = "/tmp"

# 查看当前工作目录
retval = os.getcwd()
print("当前工作目录为 %s" % retval)

# 修改当前工作目录
os.chdir(path)

# 查看修改后的工作目录
retval = os.getcwd()

print("目录修改成功 %s" % retval)
