# 1.当内部作用域想修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字了。

# 修改全局变量 num

# !/usr/bin/python3

num = 1


def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)


fun1()
print(num)

# 输出结果

# 1
# 123
# 123

print('\n')


# 2. 修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了

def outer():
    num = 10

    def inner():
        nonlocal num  # nonlocal关键字声明
        num = 100
        print(num)

    inner()
    print(num)


outer()

# 输出结果

# 100
# 100


print('\n')

# 3. 通过函数参数传递
a = 10


def test(a):
    a = a + 1
    print(a)


test(a)

# 输出结果

# 11

print('\n')

# 4. 修改 a 为全局变量

a = 10


def test():
    global a
    a = a + 1
    print(a)


test()

# 输出结果
# 11
