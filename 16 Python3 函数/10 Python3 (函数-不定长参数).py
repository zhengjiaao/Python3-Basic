# !/usr/bin/python3

# 你可能需要一个函数能处理比当初声明时更多的参数。

# 1.可写函数说明
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
printinfo(70, 60, 50)

# 输出结果

# 输出:
# 70
# (60, 50)

print('\n')


# 2.可写函数说明
# 不向函数传递未命名的变量。
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)
# 输出:
# 10
# 输出:
# 70
# 60
# 50

print('\n')


# 3.可写函数说明
# 加了两个星号 ** 的参数会以字典的形式导入
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo 函数
printinfo(1, a=2, b=3)

# 输出:
# 1
# {'a': 2, 'b': 3}

print('\n')


# 4. 声明函数时，参数中星号 * 可以单独出现
# 单独出现星号 *，则星号 * 后的参数必须用关键字传入
def f(a, b, *, c):
    return a + b + c


f(1, 2, c=3)  # 正常

f(1, 2, 3)  # 报错
