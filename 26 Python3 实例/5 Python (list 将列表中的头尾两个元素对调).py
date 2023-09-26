# 定义一个列表，并将列表中的头尾两个元素对调。

# 实现要求：
# 对调前 : [1, 2, 3]
# 对调后 : [3, 2, 1

# 1.示例
def swapList(newList):
    size = len(newList)
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    return newList


newList = [1, 2, 3]
print(swapList(newList))  # [3, 2, 1]


# 2.示例
def swapList(newList):
    newList[0], newList[-1] = newList[-1], newList[0]
    return newList


newList = [1, 2, 3]
print(swapList(newList))  # [3, 2, 1]


# 3.示例
def swapList(list):
    get = list[-1], list[0]
    list[0], list[-1] = get
    return list


newList = [1, 2, 3]
print(swapList(newList))  # [3, 2, 1]
