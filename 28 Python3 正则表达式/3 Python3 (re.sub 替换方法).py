# Python 的re模块提供了re.sub用于替换字符串中的匹配项。

# !/usr/bin/python3
import re

phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)

# 电话号码 :  2004-959-559
# 电话号码 :  2004959559
