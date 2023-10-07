# Python3 打包成exe

- [pyinstaller.org](https://pyinstaller.org/en/stable/)

## 安装

安装

```shell
pip install -U pyinstaller
```

使用

```shell
pyinstaller your_program.py
```

## 示例

创建 python 脚本:`your_program.py`

```python
#!/usr/bin/python3

import time

# 第一个注释
print("Hello, Python!")  # 第二个注释

if True:
    print("True")
else:
    print("False")

time.sleep(10)
```

打包成exe可执行文件

```shell
pyinstaller your_program.py

# or
pyinstaller -F your_program.py
```

- 执行完毕会生成【build】【dist】文件夹和【.spec】结尾的文件。
- exe文件在【dist】文件夹里面。



