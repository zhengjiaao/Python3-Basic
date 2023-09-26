# split 方法按照能够匹配的子串将字符串分割后返回列表

import re

print(re.split('\W+', 'runoob, runoob, runoob.'))
print(re.split('(\W+)', ' runoob, runoob, runoob.'))
print(re.split('\W+', ' runoob, runoob, runoob.', 1))
print(re.split('a*', 'hello world'))  # 对于一个找不到匹配的字符串而言，split 不会对其作出分割

# ['runoob', 'runoob', 'runoob', '']
# ['', ' ', 'runoob', ', ', 'runoob', ', ', 'runoob', '.', '']
# ['', 'runoob, runoob, runoob.']
# ['', 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '']
