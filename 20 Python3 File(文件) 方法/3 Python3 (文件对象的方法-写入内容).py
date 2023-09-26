# f.write() 方法，将 string 写入到文件中, 然后返回写入的字符数

# 打开一个文件
f = open("./tmp/foo.txt", "w")

num = f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
print(num)  # 29

# 关闭打开的文件
f.close()

# 写入一些不是字符串的东西, 那么将需要先进行转换
# 打开一个文件
f = open("./tmp/foo1.txt", "w")

value = ('www.runoob.com', 14)
s = str(value)
f.write(s)

# 关闭打开的文件
f.close()