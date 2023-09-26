# re.search 扫描整个字符串并返回第一个成功的匹配。

# !/usr/bin/python3

import re

print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配

# (0, 3)
# (11, 14)

print('\n')

# 2. re.match与re.search的区别
import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print("search --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

# No match!!
# search --> matchObj.group() :  dogs
