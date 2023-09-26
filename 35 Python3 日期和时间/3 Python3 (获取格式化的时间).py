#!/usr/bin/python3

import time

# 根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime()

localtime = time.asctime(time.localtime(time.time()))
print("本地时间为 :", localtime)  # 本地时间为 : Thu Apr  7 10:29:13 2016
