# 遍历数字序列
for i in range(5):
    print(i)

print('\n')

# 指定区间
for i in range(5,9) :
    print(i)

print('\n')

# 步长：以指定数字开始并指定不同的增量
for i in range(0, 10, 3) :
    print(i)

print('\n')

# 结合 range() 和 len() 函数以遍历一个序列的索引
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

print('\n')

# 使用 range() 函数来创建一个列表
print(list(range(5))) # [0, 1, 2, 3, 4]