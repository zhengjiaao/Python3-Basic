#!/usr/bin/python3

import threading
import time


# 1.线程同步 :如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步。
# 打印列表时要么全部输出0，要么全部输出1，不会再出现一半0一半1的尴尬场面

class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print("开启线程： " + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.delay, 3)
        # 释放锁，开启下一个线程
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")

# 结果输出

# 开启线程： Thread-1
# 开启线程： Thread-2
# Thread-1: Wed Sep 13 15:53:26 2023
# Thread-1: Wed Sep 13 15:53:27 2023
# Thread-1: Wed Sep 13 15:53:28 2023
# Thread-2: Wed Sep 13 15:53:30 2023
# Thread-2: Wed Sep 13 15:53:32 2023
# Thread-2: Wed Sep 13 15:53:34 2023
# 退出主线程
