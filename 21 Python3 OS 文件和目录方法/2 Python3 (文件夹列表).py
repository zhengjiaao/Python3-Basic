#!/usr/bin/python3

import os, sys

# os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。 它不包括 . 和 .. 即使它在文件夹中。

# 打开文件
path = "./var/www/html/"
dirs = os.listdir(path)

# 输出所有文件和文件夹
for file in dirs:
    print(file)
