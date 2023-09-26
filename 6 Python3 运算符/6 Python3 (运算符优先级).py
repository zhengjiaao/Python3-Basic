#!/usr/bin/python3

a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d  # ( 30 * 15 ) / 5
print("(a + b) * c / d 运算结果为：", e)  # 90.0

e = ((a + b) * c) / d  # (30 * 15 ) / 5
print("((a + b) * c) / d 运算结果为：", e)  # 90.0

e = (a + b) * (c / d)  # (30) * (15/5)
print("(a + b) * (c / d) 运算结果为：", e)  # 90.0

e = a + (b * c) / d  # 20 + (150/5)
print("a + (b * c) / d 运算结果为：", e)  # 50.0

# and 拥有更高优先级
x = True
y = False
z = False

if x or y and z:
    print("yes")
else:
    print("no")

# yes
