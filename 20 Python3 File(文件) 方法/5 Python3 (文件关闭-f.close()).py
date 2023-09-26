f = open('./tmp/foo.txt', 'rb+')
print(f.write(b'0123456789abcdef'))  # 16
# 关闭打开的文件
f.close()  # 尝试再调用该文件，则会抛出异常 f.read()


# 使用 with 关键字，在结束后, 它会帮你正确的关闭文件。
# 比 try - finally 语句块要简短
with open('./tmp/foo.txt', 'r') as f2:
    read_data = f2.read()

print(f2.closed)
