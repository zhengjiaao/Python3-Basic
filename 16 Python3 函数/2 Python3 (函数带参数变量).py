#!/usr/bin/python3

# 1.比较两个数，并返回较大的数

def max(a, b):
    if a > b:
        return a
    else:
        return b


a = 4
b = 5
print(max(a, b))  # 5


# 2.计算面积函数
def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)


print_welcome("Runoob")  # Welcome Runoob

w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))
# width = 4  height = 5  area = 20
