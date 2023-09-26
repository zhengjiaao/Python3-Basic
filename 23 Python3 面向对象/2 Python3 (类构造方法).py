#!/usr/bin/python3

# 类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用

class Complex:
    # 无参数
    # def __init__(self):
    #     print("类的实例化操作会自动调用（构造方法）")
    #     self.data = []

    # 带参数
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


# 无参数
# a = Complex()
# print(a.data)

# 带参数
x = Complex(3.0, -4.5)
print(x.r, x.i)  # 输出结果：3.0 -4.5
