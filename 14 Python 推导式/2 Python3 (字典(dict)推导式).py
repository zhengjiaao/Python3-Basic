# 使用字符串及其长度创建字典

listdemo = ['Google', 'Runoob', 'Taobao']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {key: len(key) for key in listdemo}
print(newdict)  # {'Google': 6, 'Runoob': 6, 'Taobao': 6}

# 提供三个数字，以三个数字为键，三个数字的平方为值来创建字典

dic = {x: x ** 2 for x in (2, 4, 6)}
print(dic)  # {2: 4, 4: 16, 6: 36}
print(type(dic))  # class 'dict'>
