# 类对象支持两种操作：属性引用和实例化。

# 属性引用使用和 Python 中所有的属性引用一样的标准语法：obj.name。
# 类对象创建后，类命名空间中所有的命名都是有效属性名。

# !/usr/bin/python3

class MyClass:
    """一个简单的类实例"""
    i = 12345

    def f(self):
        return 'hello world'


# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())

# 输出结果

# MyClass 类的属性 i 为： 12345
# MyClass 类的方法 f 输出为： hello world
