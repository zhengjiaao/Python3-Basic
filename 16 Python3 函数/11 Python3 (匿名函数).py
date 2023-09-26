# Python 使用 lambda 来创建匿名函数。
# 所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。

# 1. lambda 函数的语法
x = lambda a: a + 10
print(x(5))  # 15

print('\n')

# 2.匿名函数设置两个参数
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))
# 相加后的值为 :  30
# 相加后的值为 :  40

print('\n')


# 3.将匿名函数封装在一个函数内，这样可以使用同样的代码来创建多个匿名函数。
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# 22
# 33
