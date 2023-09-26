# Python 的 time 模块下有很多函数可以转换常见日期格式。如函数 time.time() 用于获取当前时间戳,

# !/usr/bin/python3

import time  # 引入time模块

ticks = time.time()
print("当前时间戳为:", ticks)  # 当前时间戳为: 1694592916.610188

# 时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。太遥远的日期也不行，UNIX和Windows只支持到2038年。
