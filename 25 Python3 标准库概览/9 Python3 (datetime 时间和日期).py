# 日期和时间
# datetime 模块为日期和时间处理同时提供了简单和复杂的方法。
# 支持日期和时间算法的同时，实现的重点放在更有效的处理和格式化输出。

import datetime

# 获取当前日期和时间
current_datetime = datetime.datetime.now()
print(current_datetime)  # 2023-09-12 17:13:25.645628

# 获取当前日期
current_date = datetime.date.today()
print(current_date)  # 2023-09-12

# 格式化日期
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)  # 输出：2023-09-12 17:13:25

# 输出结果

# 2023-09-12 17:13:25.645628
# 2023-09-12
# 2023-09-12 17:13:25

print('\n')

# 2. 该模块还支持时区处理
# 导入了 datetime 模块中的 date 类
from datetime import date

now = date.today()  # 当前日期
print(now)  # 2023-09-12

print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
# 09-12-23. 12 Sep 2023 is a Tuesday on the 12 day of September.

# 创建了一个表示生日的日期对象
birthday = date(1964, 7, 31)
age = now - birthday  # 计算两个日期之间的时间差
print(age.days)  # 变量age的days属性，表示时间差的天数
# 21592
