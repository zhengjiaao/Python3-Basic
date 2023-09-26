#!/usr/bin/python3

# 函数调用使用关键字参数来确定传入的参数值
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。


# 1.可写函数说明
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return


# 调用printme函数
printme(str="菜鸟教程") # 菜鸟教程


# 2.可写函数说明
def printinfo(name, age):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="runoob")