# Python random 模块

Python random 模块主要用于生成随机数。

random 模块实现了各种分布的伪随机数生成器。

```python
import random

# 查看 random 模块中的内容
print(dir(random))
```

输出结果：

```shell
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_inst', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
```

## 使用 random() 方法返回一个随机数

它在半开放区间 [0,1) 范围内，包含 0 但不包含 1。

```python
# 导入 random 包
import random

# 生成随机数
print(random.random())  # 0.4784904215869241
```

## seed() 方法改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数。

```python
#!/usr/bin/python3
import random

random.seed()
print("使用默认种子生成随机数：", random.random())
print("使用默认种子生成随机数：", random.random())

random.seed(10)
print("使用整数 10 种子生成随机数：", random.random())
random.seed(10)
print("使用整数 10 种子生成随机数：", random.random())

random.seed("hello", 2)
print("使用字符串种子生成随机数：", random.random())
```

输出结果：

```shell
使用默认种子生成随机数： 0.7908102856355441
使用默认种子生成随机数： 0.81038961519195
使用整数 10 种子生成随机数： 0.5714025946899135
使用整数 10 种子生成随机数： 0.5714025946899135
使用字符串种子生成随机数： 0.3537754404730722
```

## random 模块方法

random 模块方法如下：
[python-random.html](https://www.runoob.com/python3/python-random.html)

