#!/usr/bin/python3

#索引值以 0 为开始值，-1 为从末尾的开始位置
str = 'Runoob'

print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str)
print (str + "TEST") # 连接字符串


#输出

# Runoob
# Runoo
# R
# noo
# noob
# RunoobRunoob
# RunoobTEST