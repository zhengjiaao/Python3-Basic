# 把列表当做队列用, 在队列里第一加入的元素，第一个取出来。
# 但是拿列表用作这样的目的效率不高。
# 在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")

print(queue.popleft())  # Eric
print(queue.popleft())  # John
print(queue)  # deque(['Michael', 'Terry', 'Graham'])
