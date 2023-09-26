#!/usr/bin/python3

tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

del tinydict['Name']  # 删除键 'Name'
tinydict.clear()  # 清空字典
del tinydict  # 删除字典

print("tinydict['Age']: ", tinydict['Age'])  # 执行 del 操作后字典不再存在，异常：NameError: name 'tinydict' is not defined
print("tinydict['School']: ", tinydict['School'])
