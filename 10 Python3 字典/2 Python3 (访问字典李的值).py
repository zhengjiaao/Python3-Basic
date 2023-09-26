#!/usr/bin/python3

tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print("tinydict['Name']: ", tinydict['Name'])  # tinydict['Name']:  Runoob
print("tinydict['Age']: ", tinydict['Age'])  # tinydict['Age']:  7

# 如果用字典里没有的键访问数据，会输出错误
print("tinydict['Alice']: ", tinydict['Alice'])  # 报错 KeyError: 'Alice'
