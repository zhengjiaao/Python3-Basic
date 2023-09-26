#!/usr/bin/python3

import time

# 可以使用 time 模块的 strftime 方法来格式化日期

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 2023-09-13 16:26:19

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))  # Wed Sep 13 16:26:19 2023

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))  # 1459175064.0

# 输出结果

# 2023-09-13 16:26:19
# Wed Sep 13 16:26:19 2023
# 1459175064.0
