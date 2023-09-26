#!/usr/bin/python3

import _thread
import time


# 1. 创建多线程
# 语法: _thread.start_new_thread ( function, args[, kwargs] )
# 参数说明:
# function - 线程函数。
# args - 传递给线程函数的参数,他必须是个tuple类型。
# kwargs - 可选参数。


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))


# 创建两个线程
try:
    _thread.start_new_thread(print_time, ("Thread-1", 2,))
    _thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
    print("Error: 无法启动线程")

while 1:
    pass

# 执行以上程后可以按下 ctrl-c 退出。

# 输出结果

# Thread-1: Wed Sep 13 15:45:08 2023
# Thread-1: Wed Sep 13 15:45:10 2023
# Thread-2: Wed Sep 13 15:45:10 2023
# Thread-1: Wed Sep 13 15:45:12 2023
# Thread-2: Wed Sep 13 15:45:14 2023
