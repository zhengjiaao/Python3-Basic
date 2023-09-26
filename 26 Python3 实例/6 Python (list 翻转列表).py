# 定义一个列表，并将它翻转。

# 要求
# 翻转前 : list = [10, 11, 12, 13, 14, 15]
# 翻转后 : [15, 14, 13, 12, 11, 10]

# 1. reversed() 方法
def Reverse(lst):
    return [ele for ele in reversed(lst)]


lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))


# 2. reverse
def Reverse(lst):
    lst.reverse()
    return lst


lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))


# 3. lst[::-1]
def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst


lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))

# 4. 调用 list 列表的 sort 方法, 设置 reverse 为 True 即可翻转列表
li = [*range(10, 16)]
# 得到列表 li = [10, 11, 12, 13, 14, 15], * 为解包符号
print(li)
# 降序排列
li.sort(reverse=True)
print(li)


# 输出: [15, 14, 13, 12, 11, 10]

# 5. 利用 while 循环
def fanzhuan(list):
    a = []
    i = len(list)
    while i > 0:
        a.append(list[i - 1])  # 生成一个新的列表，原列表的最后一位成为第一位
        i -= 1  # 依次向前进一位
    return a


fa = fanzhuan([10, 11, 12, 13, 14, 15])
print(fa)
