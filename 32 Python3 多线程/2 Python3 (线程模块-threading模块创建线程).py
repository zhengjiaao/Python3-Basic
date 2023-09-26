#!/usr/bin/python3

import threading
import time

# 1.使用 threading 模块创建线程
# 通过直接从 threading.Thread 继承创建一个新的子类，并实例化后调用 start() 方法启动新线程，即它调用了线程的 run() 方法

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, self.delay, 5)
        print("退出线程：" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")

# 输出结果

# 开始线程：Thread-1
# 开始线程：Thread-2
# Thread-1: Wed Sep 13 15:51:15 2023
# Thread-2: Wed Sep 13 15:51:16 2023
# Thread-1: Wed Sep 13 15:51:16 2023
# Thread-1: Wed Sep 13 15:51:17 2023
# Thread-2: Wed Sep 13 15:51:18 2023
# Thread-1: Wed Sep 13 15:51:18 2023
# Thread-1: Wed Sep 13 15:51:19 2023
# 退出线程：Thread-1
# Thread-2: Wed Sep 13 15:51:20 2023
# Thread-2: Wed Sep 13 15:51:22 2023
# Thread-2: Wed Sep 13 15:51:24 2023
# 退出线程：Thread-2
# 退出主线程
