#!/usr/bin/python3

# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)  # (12, 34.56, 'abc', 'xyz')
