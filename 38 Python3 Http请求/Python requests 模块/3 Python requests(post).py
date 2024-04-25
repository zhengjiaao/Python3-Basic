# 导入 requests 包
import requests

# 发送请求
x = requests.post('https://www.runoob.com/try/ajax/demo_post.php')

# 返回网页内容
print(x.text)

# <p style='color:red;'>本内容是使用 POST 方法请求的。</p><p style='color:red;'>请求时间：
# 2023-09-26 13:35:45</p>
