#!/usr/bin/python3
# 文件名：client.py

# 导入 socket、sys 模块
import socket
import sys

# 2. 创建客户端步骤：
# 写一个简单的客户端实例连接到以上创建的服务。端口号为 9999。
# socket.connect(hostname, port ) 方法打开一个 TCP 连接到主机为 hostname 端口为 port 的服务商。
# 连接后我们就可以从服务端获取数据，记住，操作完成后需要关闭连接。


# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 9999

# 连接服务，指定主机和端口
s.connect((host, port))

# 接收小于 1024 字节的数据
msg = s.recv(1024)

s.close()

print(msg.decode('utf-8')) # 欢迎访问菜鸟教程！
