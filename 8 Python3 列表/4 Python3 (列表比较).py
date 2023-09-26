# 导入 operator 模块
import operator

a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a, b))  # operator.eq(a,b):  False
print("operator.eq(c,b): ", operator.eq(c, b))  # operator.eq(c,b):  True
