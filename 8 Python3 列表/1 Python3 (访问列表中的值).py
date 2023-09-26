# !/usr/bin/python3

# 创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。

# 正向索引
list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print(list[0])  # red
print(list[1])  # green
print(list[2])  # blue

# 反向索引
print(list[-1])  # black
print(list[-2])  # white
print(list[-3])  # yellow

# 读取指定范围内的值
print(list[0:4])  # ['red', 'green', 'blue', 'yellow']

# 从第二位开始（包含）截取到倒数第二位（不包含）
print("list[1:-2]: ", list[1:-2])  # ['green', 'blue', 'yellow']
