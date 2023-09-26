num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("num_int 数据类型为:", type(num_int))
print("num_flo 数据类型为:", type(num_flo))

print("num_new 值为:", num_new)
print("num_new 数据类型为:", type(num_new))

# 输出结果

# num_int 数据类型为: <class 'int'>
# num_flo 数据类型为: <class 'float'>
# num_new 值为: 124.23
# num_new 数据类型为: <class 'float'>


num_str = "456"
print("num_int 数据类型为:", type(num_int))
print("num_str 数据类型为:", type(num_str))

print(num_int + num_str)  # 会报错报错，输出 TypeError。 Python 在这种情况下无法使用隐式转换
