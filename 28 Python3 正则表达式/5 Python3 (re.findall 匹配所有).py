# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果有多个匹配模式，则返回元组列表，如果没有找到匹配的，则返回空列表。
# 注意： match 和 search 是匹配一次 findall 匹配所有。

# 格式：
# re.findall(pattern, string, flags=0)
# 或
# pattern.findall(string[, pos[, endpos]])


import re

# 1. 查找字符串中的所有数字，并返回查询的结果(以列表形式返回)
result1 = re.findall(r'\d+', 'runoob 123 google 456')

pattern = re.compile(r'\d+')  # 查找数字
result2 = pattern.findall('runoob 123 google 456')
result3 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)
print(result3)

# ['123', '456']
# ['123', '456']
# ['88', '12']


# 2. 多个匹配模式，返回元组列表

import re

result = re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
print(result)

# [('width', '20'), ('height', '10')]
