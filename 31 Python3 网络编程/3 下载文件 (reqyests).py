import requests

url = 'https://www.example.com/file.txt'

filename = 'file.txt'
# filename = 'D:\\file.txt'

r = requests.get(url)

# 下载文件
with open(filename, 'wb') as f:
    f.write(r.content)


