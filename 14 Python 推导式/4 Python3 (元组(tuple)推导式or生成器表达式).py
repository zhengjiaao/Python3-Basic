# 生成一个包含数字 1~9 的元组

a = (x for x in range(1, 10))
print(a)  # 返回的是生成器对象 <generator object <genexpr> at 0x0000029C19E2F5A0>
print(tuple(a))  # 使用 tuple() 函数，可以直接将生成器对象转换成元组
# (1, 2, 3, 4, 5, 6, 7, 8, 9)
