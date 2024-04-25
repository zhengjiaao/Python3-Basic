import urllib
from urllib.request import urlopen

# 1.校验网页是否存在
# 在对网页进行抓取时，经常需要判断网页是否可以正常访问，返回 200 说明网页正常，返回 404 说明网页不存在
myURL1 = urllib.request.urlopen("https://www.runoob.com/")
print(myURL1.getcode())  # 200

try:
    myURL2 = urllib.request.urlopen("https://www.runoob.com/no.html")
except urllib.error.HTTPError as e:
    if e.code == 404:
        print(404)  # 404
