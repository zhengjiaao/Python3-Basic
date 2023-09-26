#!/usr/bin/python3

# return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。
# 不带参数值的 return 语句返回 None。

# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total


# 调用sum函数
total = sum(10, 20)
print("函数外 : ", total)

# 函数内 :  30
# 函数外 :  30
