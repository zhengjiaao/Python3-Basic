# 定义一个整型数组，并计算元素之和。

# 实现要求：
# 输入 : arr[] = {1, 2, 3}
# 输出 : 6
# 计算: 1 + 2 + 3 = 6


# 1. 用for循环实现
list = [1, 2, 3]
sum = 0
for i in range(0, len(list)):
    sum += list[i]
print(sum)  # 6

# 2. 用 reduce lambda实现
from functools import reduce

list = [1, 2, 3]

print(reduce(lambda x, y: x + y, list))  # 6

