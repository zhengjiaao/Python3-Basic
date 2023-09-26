import sys

# 最后一个except子句可以忽略异常的名称，它将被当作通配符使用。
# 可以使用这种方法打印一个错误信息，然后再次把异常抛出。

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
