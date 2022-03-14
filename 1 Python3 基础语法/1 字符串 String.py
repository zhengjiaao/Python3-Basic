#!/usr/bin/python3

str = '123456789'

print(str)  # 输出字符串 123456789
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符    12345678
print(str[0])  # 输出字符串第一个字符 1
print(str[2:5])  # 输出从第三个开始到第五个的字符  345
print(str[2:])  # 输出从第三个开始后的所有字符    3456789
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2） 24
print(str * 2)  # 输出字符串两次   123456789123456789
print(str + '你好')  # 连接字符串  123456789你好

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符  hello 换行 runoob
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义  hello\nrunoob
