# 1. os.replace() 方法用于重命名文件或目录。

import os

# 重命名文件或目录
os.replace('./tmp/google.txt', './tmp/runoob.txt')

# 重命名文件或目录
os.replace('./tmp/test1.txt', './tmp/test2.txt')

# 2. os.rename() 方法用于命名文件或目录，从 src 到 dst,如果dst是一个存在的目录, 将抛出OSError。

import os, sys

# 列出目录
print("目录为: %s" % os.listdir(os.getcwd()))

# 重命名
os.rename("test", "test2")

print("重命名成功。")

# 列出重命名后的目录
print("目录为: %s" % os.listdir(os.getcwd()))
