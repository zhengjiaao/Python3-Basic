# try 语句还有另外一个可选的子句，它定义了无论在任何情况下都会执行的清理行为。
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
