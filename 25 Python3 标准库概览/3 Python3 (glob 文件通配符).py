# 文件通配符
# glob模块提供了一个函数用于从目录通配符搜索中生成文件列表

import glob

print(glob.glob('*.py'))
# ['1 Python3 (os 操作系统函数).py', '2 Python3 (shutil 文件和目录管理).py', '3 Python3 (glob 文件通配符).py']
