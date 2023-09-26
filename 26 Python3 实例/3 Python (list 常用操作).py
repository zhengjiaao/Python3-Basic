# list 定义
li = ["a", "b", "mpilgrim", "z", 'example', "example"]
print(li)

print('\n list 索引')

print(li[1])
print(li[0:3])

# b
# ['a', 'b', 'mpilgrim']

print('\n list 负数索引')

# list 负数索引
print(li[-1])
print(li[1:-1])

# example
# ['b', 'mpilgrim', 'z', 'example']

print('\n list 搜索')

# list 搜索
print(li.index("b"))
# print(li.index("c")) # 不存在的元素,则抛异常
print("c" in li)  # 检验存在元素 返回 True or False

# 1
# False

print('\n list 删除元素')

# list 删除元素

li.remove("example")  # 删除首次出现的一个值，第二个 'example'未删除，删除不存在元素，则抛异常
print(li)
print(li.pop())  # pop 会做两件事: 删除 list 的最后一个元素, 然后返回删除元素的值。
print(li)

# ['a', 'b', 'mpilgrim', 'z', 'example']
# example
# ['a', 'b', 'mpilgrim', 'z']

print('\n list 运算符')

# list 运算符
li2 = ['a', 'b', 'mpilgrim']
li2 = li2 + ['example', 'new']
print(li2)
li2 += ['two']
print(li2)
li3 = [1, 2] * 3
print(li3)

# ['a', 'b', 'mpilgrim', 'example', 'new']
# ['a', 'b', 'mpilgrim', 'example', 'new', 'two']
# [1, 2, 1, 2, 1, 2]

print('\n 使用 join 把 list 转为 字符串')

# 使用join链接list成为字符串
params = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}
print(["%s=%s" % (k, v) for k, v in params.items()])
print(";".join(["%s=%s" % (k, v) for k, v in params.items()]))

# ['server=mpilgrim', 'database=master', 'uid=sa', 'pwd=secret']
# server=mpilgrim;database=master;uid=sa;pwd=secret

print('\n list 分割字符串')

# list 分割字符串
li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s = ";".join(li)
print(s)
print(s.split(";"))
print(s.split(";", 1))

# server=mpilgrim;uid=sa;database=master;pwd=secret
# ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
# ['server=mpilgrim', 'uid=sa;database=master;pwd=secret']

print('\n list 的映射解析')

# list 的映射解析
li = [1, 9, 8, 4]
print([elem * 2 for elem in li])
print(li)
li = [elem * 2 for elem in li]
print(li)

print('\n dictionary 中的解析')

# 字典 dictionary 中的解析
params = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}
print(params.keys())
print(params.values())
print(params.items())
print([k for k, v in params.items()])
print([v for k, v in params.items()])
print(["%s=%s" % (k, v) for k, v in params.items()])

# dict_keys(['server', 'database', 'uid', 'pwd'])
# dict_values(['mpilgrim', 'master', 'sa', 'secret'])
# dict_items([('server', 'mpilgrim'), ('database', 'master'), ('uid', 'sa'), ('pwd', 'secret')])
# ['server', 'database', 'uid', 'pwd']
# ['mpilgrim', 'master', 'sa', 'secret']
# ['server=mpilgrim', 'database=master', 'uid=sa', 'pwd=secret']

print('\n list 过滤')

# list 过滤
li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]

print([elem for elem in li if len(elem) > 1])
print([elem for elem in li if elem != "b"])
print([elem for elem in li if li.count(elem) == 1])

# ['mpilgrim', 'foo']
# ['a', 'mpilgrim', 'foo', 'c', 'd', 'd']
# ['a', 'mpilgrim', 'foo', 'c']
