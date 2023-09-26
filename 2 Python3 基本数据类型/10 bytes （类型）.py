x = b"hello"
y = x[1:3]  # 切片操作，得到 b"el"
z = x + b"world"  # 拼接操作，得到 b"helloworld"

print(y)  # b'el'
print(z)  # b'helloworld'
