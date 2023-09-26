#!/usr/bin/python3

import time

# 从返回浮点数的时间戳方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。

localtime = time.localtime(time.time())
print("本地时间为 :", localtime)
# 本地时间为 : time.struct_time(tm_year=2023, tm_mon=9, tm_mday=13, tm_hour=16, tm_min=23, tm_sec=25, tm_wday=2, tm_yday=256, tm_isdst=0)
