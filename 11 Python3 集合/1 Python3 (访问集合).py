# 集合（set）是一个无序的不重复元素序列。
# 集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。
# 可以使用大括号 { } 创建集合，元素之间用逗号 , 分隔， 或者也可以使用 set() 函数创建集合。

# 创建集合
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

# 去重功能
print(basket)  # {'orange', 'banana', 'pear', 'apple'}

# 判断存在
print('orange' in basket)  # True
print('crabgrass' in basket)  # False

# 下面展示两个集合间的运算
a = set('abracadabra')
b = set('alacazam')

print(a)  # {'d', 'c', 'a', 'b', 'r'}

print(a - b)  # {'d', 'b', 'r'}
print(a | b)  # {'d', 'l', 'z', 'c', 'a', 'm', 'b', 'r'}
print(a & b)  # {'a', 'c'}
print(a ^ b)  # {'l', 'z', 'm', 'd', 'b', 'r'}


# 集合推导式
h = {x for x in 'abracadabra' if x not in 'abc'}
print(h)  # {'r', 'd'}  每次都不一样
