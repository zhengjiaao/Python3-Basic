# Python 使用 raise 语句抛出一个指定的异常。

x = 10
if x > 5:
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))

#     raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
# Exception: x 不能大于 5。x 的值为: 10
