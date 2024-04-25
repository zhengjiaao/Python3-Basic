import urllib
from urllib.request import urlopen

# 1. 使用 urlopen 打开一个 URL
myURL = urlopen("https://www.runoob.com/")
# 2.使用 read() 函数获取网页的 HTML 实体代码
print(myURL.read())

print('\n')

# 3.read() 是读取整个网页内容，我们可以指定读取的长度
print(myURL.read(300))

print('\n')

# 4. 读取一行内容
print(myURL.readline())

# 5. 读取文件的全部内容，它会把读取的内容赋值给一个列表变量
lines = myURL.readlines()
for line in lines:
    print(line)

# 6. 要将抓取的网页保存到本地

myURL = urlopen("https://www.runoob.com/")
f = open("runoob_urllib_test.html", "wb")
content = myURL.read()  # 读取网页内容
f.write(content)
f.close()


