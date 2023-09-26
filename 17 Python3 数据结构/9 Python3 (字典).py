# 字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。
# 无序的键=>值对集合。在同一个字典之内，关键字必须是互不相同。
# 一对大括号创建一个空的字典：{}

# 1.简单示例
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127

print(tel)  # {'jack': 4098, 'sape': 4139, 'guido': 4127}
print(tel['jack'])  # 4098

del tel['sape']
print(tel)  # {'jack': 4098, 'guido': 4127}

tel['irv'] = 4127
print(tel)  # {'jack': 4098, 'guido': 4127, 'irv': 4127}

print(list(tel.keys()))  # ['jack', 'guido', 'irv']
print(sorted(tel.keys()))  # ['guido', 'irv', 'jack']

print('guido' in tel)  # True
print('jack' not in tel)  # False

print('\n')

# 2.构造函数 dict() 直接从键值对元组列表中构建字典。如果有固定的模式，列表推导式指定特定的键值对
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
# {'sape': 4139, 'guido': 4127, 'jack': 4098}

print('\n')

# 3.字典推导可以用来创建任意键和值的表达式词典
print({x: x ** 2 for x in (2, 4, 6)})
# {2: 4, 4: 16, 6: 36}

print('\n')

# 4.如果关键字只是简单的字符串，使用关键字参数指定键值对有时候更方便
print(dict(sape=4139, guido=4127, jack=4098))
# {'sape': 4139, 'guido': 4127, 'jack': 4098}
