## os.makedirs() 方法

os.makedirs() 方法用于递归创建多层目录。

如果子目录创建失败或者已经存在，会抛出一个 OSError 的异常，Windows上Error 183 即为目录已经存在的异常错误。

如果第一个参数 path 只有一级，即只创建一层目录，则与 [mkdir()](https://www.runoob.com/python3/python3-os-mkdir.html) 函数相同。

### 语法

**makedirs()**方法语法格式如下：

```
os.makedirs(name, mode=511, exist_ok=False)
```

### 参数

- **path** -- 需要递归创建的目录，可以是相对或者绝对路径。
- **mode** -- 权限模式，默认的模式为 511 (八进制)。。
- **exist_ok**：是否在目录存在时触发异常。如果 exist_ok 为 False（默认值），则在目标目录已存在的情况下触发 FileExistsError
  异常；如果 exist_ok 为 True，则在目标目录已存在的情况下不会触发 FileExistsError 异常。