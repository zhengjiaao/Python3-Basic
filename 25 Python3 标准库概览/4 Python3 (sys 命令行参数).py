# 通用工具脚本经常调用命令行参数。
# 这些命令行参数以链表形式存储于 sys 模块的 argv 变量。

import sys

print(sys.argv)

# 错误输出重定向和程序终止
print(sys.stderr.write('Warning, log file not found starting a new one\n'))
# 大多脚本的定向终止都使用
sys.exit()
