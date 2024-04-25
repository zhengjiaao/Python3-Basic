from pymongo import MongoClient
from gridfs import GridFS

# 连接到 MongoDB
# 1.有密码连接，有认证
client = MongoClient("mongodb://myUserTest:123456@localhost:27017/admin")  # admin 是认证数据库

# 2.连接数据库
# 注意: 在 MongoDB 中，数据库只有在内容插入后才会创建! 就是说，数据库创建后要创建集合(数据表)并插入一个文档(记录)，数据库才会真正创建。
db = client["testdb"]

# 验证数据库存在
dblist = client.list_database_names()
if "testdb" in dblist:
    print("数据库已存在！")

# 选择 GridFS 存储桶
fs = GridFS(db)

# 写入文件
with open('my_file.txt', 'w') as file:
    file.write('Hello, World!')

# 读取文件内容
with open('my_file.txt', 'r') as file:
    content = file.read()
    print(content)

# 上传文件
with open('my_file.txt', 'rb') as file:
    file_id = fs.put(file, filename='my_file.txt')
    print("文件上传成功，_id:", file_id)

# 根据 _id 读取文件
file = fs.get(file_id)
if file:
    print(f"文件 '{file.filename}' 存在于 MongoDB 中。")
else:
    print(f"文件 '{file.filename}' 不存在于 MongoDB 中。")

if file:
    data = file.read()
    print(data)

# 根据 filename 读取文件
# file = fs.find_one({'filename': 'my_file.txt'})
# if file:
#     data = file.read()
#     print(data)

# 下载文件
with open('downloaded_file.txt', 'wb') as file:
    file.write(data)

# 删除文件
fs.delete(file_id)
print("文件删除成功")