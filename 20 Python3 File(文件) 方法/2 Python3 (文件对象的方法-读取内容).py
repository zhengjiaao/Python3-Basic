#!/usr/bin/python3

# f.read() 方法，读取一个文件的内容

# 打开一个文件
f = open("/tmp/foo.txt", "r")

str = f.read()
print(str)

# 关闭打开的文件
f.close()

# f.readline() 方法，会从文件中读取单独的一行

# 打开一个文件
f = open("/tmp/foo.txt", "r")

str = f.readline()
print(str)  # Python 是一个非常好的语言。

# 关闭打开的文件
f.close()

# f.readlines() 方法，将返回该文件中包含的所有行

# 打开一个文件
f = open("/tmp/foo.txt", "r")

str = f.readlines()
print(str)  # ['Python 是一个非常好的语言。\n', '是的，的确非常好!!\n']

# 关闭打开的文件
f.close()

# 迭代一个文件对象然后读取每行

# 打开一个文件
f = open("/tmp/foo.txt", "r")

for line in f:
    print(line, end='')

# 关闭打开的文件
f.close()
