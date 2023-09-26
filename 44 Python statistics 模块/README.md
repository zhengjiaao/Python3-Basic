# Python statistics 模块

Python statistics 是标准库中的一个模块，模块提供了许多基本统计计算的函数。

statistics 模块是在 Python 3.4 版本中新增加的，可以帮助我们分析和计算数据集的统计特征。

```python
import statistics

# 查看模块
print(dir(statistics))
```

### math 模块方法

| 方法                                                                                         | 描述                           |
|:-------------------------------------------------------------------------------------------|:-----------------------------|
| [statistics.harmonic_mean()](https://www.runoob.com/python3/ref-stat-harmonic_mean.html)   | 计算给定数据集的调和平均值。               |
| [statistics.mean()](https://www.runoob.com/python3/ref-stat-mean.html)                     | 计算数据集的平均值                    |
| [statistics.median()](https://www.runoob.com/python3/ref-stat-median.html)                 | 计算数据集的中位数                    |
| [statistics.median_grouped()](https://www.runoob.com/python3/ref-stat-median_grouped.html) | 计算给定分组数据集的分组中位数              |
| [statistics.median_high()](https://www.runoob.com/python3/ref-stat-median_high.html)       | 计算给定数据集的高位中位数                |
| [statistics.median_low()](https://www.runoob.com/python3/ref-stat-median_low.html)         | 计算给定数据集的低位中位数。               |
| [statistics.mode()](https://www.runoob.com/python3/ref-stat-mode.html)                     | 算数据集的众数（出现频率最高的值）            |
| [statistics.pstdev()](https://www.runoob.com/python3/ref-stat-pstdev.html)                 | 计算给定数据集的样本标准偏差               |
| [statistics.stdev()](https://www.runoob.com/python3/ref-stat-stdev.html)                   | 计算数据集的标准差                    |
| [statistics.pvariance()](https://www.runoob.com/python3/ref-stat-pvariance.html)           | 计算给定数据集的样本方差                 |
| [statistics.variance()](https://www.runoob.com/python3/ref-stat-variance.html)             | 计算数据集的方差                     |
| [statistics.quantiles()](https://www.runoob.com/python3/ref-stat-quantiles.html)           | 计算数据集的分位数，可指定分位数的数量（默认为四分位数） |
