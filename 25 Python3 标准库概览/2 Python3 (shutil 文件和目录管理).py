# 针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口
import shutil

# 必须使用绝对路径，好像不支持相对路径
shutil.copyfile('D:\\python\\tmp\\test.txt', 'D:\\python\\tmp\\test2.txt')
shutil.move('D:\\python\\tmp', 'D:\\python\\tmp2')