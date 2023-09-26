# 通过 id() 函数来查看内存地址变化

def change(a):
    print(id(a))  # 指向的是同一个对象
    a = 10
    print(id(a))  # 一个新对象


a = 1
print(id(a))
change(a)

# 2270406377712
# 2270406377712
# 2270406378000
