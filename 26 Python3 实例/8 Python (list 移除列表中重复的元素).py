# 从列表中删除重复的元素。


# 1. set
list_1 = [1, 2, 1, 4, 6]
print(list(set(list_1)))  # [1, 2, 4, 6]

# 2.删除两个列表中重复的元素
list_1 = [1, 2, 1, 4, 6]
list_2 = [7, 8, 2, 1]

# 使用 ^ 运算符得到两个列表的对称差
print(list(set(list_1) ^ set(list_2)))  # [4, 6, 7, 8]

# 3.去除单个列表中的重复元素，且顺序保持不变
list_case = [9, 9, 9, 8, 7, 6, 6, 6, 4, 3, 5, 3, 5, 2]
re = []
for x in list_case:
    if x in re:
        continue
    else:
        re.append(x)

print(re)  # [9, 8, 7, 6, 4, 3, 5, 2]
