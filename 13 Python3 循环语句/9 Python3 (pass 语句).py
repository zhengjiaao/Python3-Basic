#!/usr/bin/python3

# Python pass是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句

# 在字母为 o 时 执行 pass 语句块

for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")
