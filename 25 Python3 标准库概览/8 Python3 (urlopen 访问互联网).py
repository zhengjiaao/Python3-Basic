# 有几个模块用于访问互联网以及处理网络通信协议。
# 其中最简单的两个是用于处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib:

from urllib.request import urlopen

for line in urlopen('https://docs.python.org/zh-cn/3/library/index.html'):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    if 'EST' in line or 'EDT' in line:  # look for Eastern Time
        print(line)
