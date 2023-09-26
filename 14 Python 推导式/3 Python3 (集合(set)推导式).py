# 计算数字 1,2,3 的平方数
setnew = {i ** 2 for i in (1, 2, 3)}
print(setnew)  # {1, 4, 9}

# 判断不是 abc 的字母并输出
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)  # {'d', 'r'}
print(type(a))  # <class 'set'>
