# 操作系统接口
# os模块提供了不少与操作系统相关联的函数。

import os

print(os.getcwd())  # 返回当前的工作目录

os.chdir('D:\gitTmp\data')  # 修改当前的工作目录
print(os.getcwd())

os.system('mkdir today')  # 执行系统命令 mkdir