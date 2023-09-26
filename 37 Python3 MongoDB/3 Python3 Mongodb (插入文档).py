#!/usr/bin/python3

import pymongo

# 1.有密码连接，有认证
myclient = pymongo.MongoClient("mongodb://myUserTest:123456@localhost:27017/admin")  # admin 是认证数据库

mydb = myclient["testdb"]  # 数据库
mycol = mydb["sites"]  # 集合

# 2. 插入单个文档
mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}

x = mycol.insert_one(mydict)
print(x)

# 2.2 返回 _id 字段
print(x.inserted_id)  # 6507baf2c481cc80bf366324

# 3. 插入多个文档  insert_many()
mylist = [
    {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
    {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
    {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
    {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
    {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
]

x = mycol.insert_many(mylist)

# 输出插入的所有文档对应的 _id 值
print(x.inserted_ids)
# [ObjectId('6507bb47b3619adfe19955ad'), ObjectId('6507bb47b3619adfe19955ae'), ObjectId('6507bb47b3619adfe19955af'), ObjectId('6507bb47b3619adfe19955b0'), ObjectId('6507bb47b3619adfe19955b1')]

# 4.插入指定 _id 的多个文档
mylist = [
    {"_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
    {"_id": 2, "name": "Google", "address": "Google 搜索"},
    {"_id": 3, "name": "Facebook", "address": "脸书"},
    {"_id": 4, "name": "Taobao", "address": "淘宝"},
    {"_id": 5, "name": "Zhihu", "address": "知乎"}
]

x = mycol.insert_many(mylist)

# 输出插入的所有文档对应的 _id 值
print(x.inserted_ids)
# [1, 2, 3, 4, 5]
