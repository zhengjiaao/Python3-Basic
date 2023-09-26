# 集合：集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。

# 可以用大括号({})创建集合。注意：如果要创建一个空集合，你必须用 set() 而不是 {}

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

# 删除重复的
print(basket)

# 检测成员
print('orange' in basket)  # True
print('crabgrass' in basket)  # False

print('\n')

# 以下演示了两个集合的操作
a = set('abracadabra')
b = set('alacazam')

print(a)  # a 中唯一的字母

print(a - b)  # 在 a 中的字母，但不在 b 中
print(a | b)  # 在 a 或 b 中的字母
print(a & b)  # 在 a 和 b 中都有的字母
print(a ^ b)  # 在 a 或 b 中的字母，但不同时在 a 和 b 中

print('\n')

# 集合也支持推导式
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)  # {'r', 'd'}
