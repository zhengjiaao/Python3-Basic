# f.seek() 方法，改变文件指针当前的位置, 可以使用 f.seek(offset, from_what) 函数
f = open('./tmp/foo.txt', 'rb+')

print(f.write(b'0123456789abcdef'))  # 16
print(f.seek(5))  # 移动到文件的第六个字节 5
print(f.read(1))  # b'5'
print(f.seek(-3, 2))  # 移动到文件的倒数第三字节 13
print(f.read(1))  # b'd'

# 关闭打开的文件
f.close()
