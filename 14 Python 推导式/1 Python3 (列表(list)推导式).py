# Python 推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列的结构体。


# 过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母

names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)  # ['ALICE', 'JERRY', 'WENDY', 'SMITH']

# 计算 30 以内可以被 3 整除的整数

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)  # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
