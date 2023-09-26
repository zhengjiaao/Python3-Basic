# Python3 日期和时间

Python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间。

时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。太遥远的日期也不行，UNIX和Windows只支持到2038年。

## 什么是时间元组？

很多Python函数用一个元组装起来的9组数字处理时间:

| 序号 | 字段     | 值                        |
|:---|:-------|:-------------------------|
| 0  | 4位数年   | 2008                     |
| 1  | 月      | 1 到 12                   |
| 2  | 日      | 1到31                     |
| 3  | 小时     | 0到23                     |
| 4  | 分钟     | 0到59                     |
| 5  | 秒      | 0到61 (60或61 是闰秒)         |
| 6  | 一周的第几日 | 0到6 (0是周一)               |
| 7  | 一年的第几日 | 1到366 (儒略历)              |
| 8  | 夏令时    | -1, 0, 1, -1是决定是否为夏令时的标识 |

上述也就是 struct_time 元组。这种结构具有如下属性：

| 序号 | 属性       | 值                                      |
|:---|:---------|:---------------------------------------|
| 0  | tm_year  | 2008                                   |
| 1  | tm_mon   | 1 到 12                                 |
| 2  | tm_mday  | 1 到 31                                 |
| 3  | tm_hour  | 0 到 23                                 |
| 4  | tm_min   | 0 到 59                                 |
| 5  | tm_sec   | 0 到 61 (60或61 是闰秒)                     |
| 6  | tm_wday  | 0 到 6 (0是周一)                           |
| 7  | tm_yday  | 一年中的第几天，1 到 366                        |
| 8  | tm_isdst | 是否为夏令时，值有：1(夏令时)、0(不是夏令时)、-1(未知)，默认 -1 |

### 获取当前时间

从返回浮点数的时间戳方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。

```python
#!/usr/bin/python3

import time

localtime = time.localtime(time.time())
print("本地时间为 :", localtime)
```

以上实例输出结果：

```
本地时间为 : time.struct_time(tm_year=2016, tm_mon=4, tm_mday=7, tm_hour=10, tm_min=28, tm_sec=49, tm_wday=3, tm_yday=98, tm_isdst=0)
```

------

### 获取格式化的时间

你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():

```python
#!/usr/bin/python3

import time

localtime = time.asctime(time.localtime(time.time()))
print("本地时间为 :", localtime)
```

以上实例输出结果：

```
本地时间为 : Thu Apr  7 10:29:13 2016
```

------

### 格式化日期

我们可以使用 time 模块的 strftime 方法来格式化日期：

```
time.strftime(format[, t])
```

#### 实例

```python
#!/usr/bin/python3

import time

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
```

以上实例输出结果：

```shell
2016-04-07 10:29:46
Thu Apr 07 10:29:46 2016
1459175064.0
```

python中时间日期格式化符号：

* %y 两位数的年份表示（00-99）
* %Y 四位数的年份表示（000-9999）
* %m 月份（01-12）
* %d 月内中的一天（0-31）
* %H 24小时制小时数（0-23）
* %I 12小时制小时数（01-12）
* %M 分钟数（00=59）
* %S 秒（00-59）
* %a 本地简化星期名称
* %A 本地完整星期名称
* %b 本地简化的月份名称
* %B 本地完整的月份名称
* %c 本地相应的日期表示和时间表示
* %j 年内的一天（001-366）
* %p 本地A.M.或P.M.的等价符
* %U 一年中的星期数（00-53）星期天为星期的开始
* %w 星期（0-6），星期天为星期的开始
* %W 一年中的星期数（00-53）星期一为星期的开始
* %x 本地相应的日期表示
* %X 本地相应的时间表示
* %Z 当前时区的名称
* %% %号本身

## Time 模块

Time 模块包含了以下内置函数，既有时间处理的，也有转换时间格式的。

更多参看 [python3-date-time.html](https://www.runoob.com/python3/python3-date-time.html)