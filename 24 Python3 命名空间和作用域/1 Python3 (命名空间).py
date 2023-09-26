# 一般有三种命名空间：
# 内置名称（built-in names）， Python 语言内置的名称，比如函数名 abs、char 和异常名称 BaseException、Exception 等等。
# 全局名称（global names），模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
# 局部名称（local names），函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）

# 查找顺序：
# 假设我们要使用变量 runoob，则 Python 的查找顺序为：局部的命名空间 -> 全局命名空间 -> 内置命名空间。
# 如果找不到变量 runoob，它将放弃查找并引发一个 NameError 异常.

# var1 是全局名称
var1 = 5


def some_func():
    # var2 是局部名称
    var2 = 6

    def some_inner_func():
        # var3 是内嵌的局部名称
        var3 = 7
