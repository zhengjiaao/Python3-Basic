#!/usr/bin/python3

import calendar

# Calendar 模块有很广泛的方法用来处理年历和月历，例如打印某月的月历

cal = calendar.month(2016, 1)
print("以下输出2016年1月份的日历:")
print(cal)

# 以下输出2016年1月份的日历:
#     January 2016
# Mo Tu We Th Fr Sa Su
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31
