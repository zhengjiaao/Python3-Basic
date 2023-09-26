# 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。

import re

it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match.group())

# 12
# 32
# 43
# 3
