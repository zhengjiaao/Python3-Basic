# str.format() 的基本使用

# 参数替换
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))  # 菜鸟教程网址： "www.runoob.com!"

# 在括号中的数字用于指向传入对象在 format() 中的位置
print('{0} 和 {1}'.format('Google', 'Runoob'))  # Google 和 Runoob
print('{1} 和 {0}'.format('Google', 'Runoob'))  # Runoob 和 Google

# 关键字参数的名字
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
# 菜鸟教程网址： www.runoob.com

# 位置及关键字参数可以任意的结合
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
# 站点列表 Google, Runoob, 和 Taobao。

# !a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化
import math

print('常量 PI 的值近似为： {}。'.format(math.pi))
# 常量 PI 的值近似为： 3.141592653589793。
print('常量 PI 的值近似为： {!r}。'.format(math.pi))
# 常量 PI 的值近似为： 3.141592653589793。
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
# 常量 PI 的值近似为 3.142。

# 在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))

# Google     ==>          1
# Runoob     ==>          2
# Taobao     ==>          3

# 有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
# Runoob: 2; Google: 1; Taobao: 3
# 也可以通过在 table 变量前使用 ** 来实现相同的功能
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))
# Runoob: 2; Google: 1; Taobao: 3
