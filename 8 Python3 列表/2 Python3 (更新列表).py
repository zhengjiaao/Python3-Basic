#!/usr/bin/python3

list = ['Google', 'Runoob', 1997, 2000]

print("第三个元素为 : ", list[2])
list[2] = 2001
print("更新后的第三个元素为 : ", list[2])

list1 = ['Google', 'Runoob', 'Taobao']
list1.append('Baidu')
print("更新后的列表 : ", list1)

# 输出结果

# 第三个元素为 :  1997
# 更新后的第三个元素为 :  2001
# 更新后的列表 :  ['Google', 'Runoob', 'Taobao', 'Baidu']
