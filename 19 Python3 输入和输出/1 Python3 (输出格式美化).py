# 1.简单示例
s = 'Hello, Runoob'

print(str(s))  # Hello, Runoob
print(repr(s))  # 'Hello, Runoob'
print(str(1 / 7))  # 0.14285714285714285

x = 10 * 3.25
y = 200 * 200
s = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
print(s)  # x 的值为： 32.5,  y 的值为：40000...

#  repr() 函数可以转义字符串中的特殊字符
hello = 'hello, runoob\n'
hellos = repr(hello)
print(hellos)  # 'hello, runoob\n'

# repr() 的参数可以是 Python 的任何对象
print(repr((x, y, ('Google', 'Runoob'))))  # (32.5, 40000, ('Google', 'Runoob'))

print('\n')

# 2.两种方式输出一个平方与立方的表
# 字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    # 注意前一行 'end' 的使用
    print(repr(x * x * x).rjust(4))

print('\n')

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

# 方法 zfill(), 它会在数字的左边填充 0
print('12'.zfill(5))  # '00012'
print('-3.14'.zfill(7))  # '-003.14'
print('3.14159265359'.zfill(5))  # '3.14159265359'
