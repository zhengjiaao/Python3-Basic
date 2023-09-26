# open() 将会返回一个 file 对象
# 语法 open(filename, mode)

# 1.write() 方法

# 打开一个文件
f = open("./tmp/foo.txt", "w")

f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")

# 关闭打开的文件
f.close()

# 2.read() 方法

# 打开一个文件
f = open("/tmp/foo.txt", "r")

str = f.read()
print(str)

# 关闭打开的文件
f.close()
