#!/usr/bin/python3

# 可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。

# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)  # 函数内取值:  [10, 20, 30, [1, 2, 3, 4]]
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)  # 函数外取值:  [10, 20, 30, [1, 2, 3, 4]]
