# 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
# 生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。

# 使用 yield 语句逐步产生从 n 到 1 的倒数数字

def countdown(n):
    while n > 0:
        yield n
        n -= 1


# 创建生成器对象
generator = countdown(5)

# 通过迭代生成器获取值
print(next(generator))  # 输出: 5
print(next(generator))  # 输出: 4
print(next(generator))  # 输出: 3

# 使用 for 循环迭代生成器
for value in generator:
    print(value)  # 输出: 2 1

# 结果输出

# 5
# 4
# 3
# 2
# 1
