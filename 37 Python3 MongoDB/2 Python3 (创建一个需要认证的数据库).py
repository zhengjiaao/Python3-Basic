#!/usr/bin/python3

import pymongo

# 1.有密码连接，有认证
myclient = pymongo.MongoClient("mongodb://myUserTest:123456@localhost:27017/admin")  # admin 是认证数据库

# 2.连接数据库
# 注意: 在 MongoDB 中，数据库只有在内容插入后才会创建! 就是说，数据库创建后要创建集合(数据表)并插入一个文档(记录)，数据库才会真正创建。
mydb = myclient["testdb"]

# 验证数据库存在
dblist = myclient.list_database_names()
# dblist = myclient.database_names()
if "testdb" in dblist:
    print("数据库已存在！")

# 3.创建集合
# 注意: 在 MongoDB 中，集合只有在内容插入后才会创建! 就是说，创建集合(数据表)后要再插入一个文档(记录)，集合才会真正创建。
# MongoDB 中的集合类似 SQL 的表。
mycol = mydb["sites"]

# 验证集合是否存在
collist = mydb.list_collection_names()
# collist = mydb.collection_names()
if "sites" in collist:  # 判断 sites 集合是否存在
    print("集合已存在！")

# 4.向集合中插入一条数据
mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}

x = mycol.insert_one(mydict)
print(x)
print(x)

# 验证数据库存在
dblist = myclient.list_database_names()
# dblist = myclient.database_names()
if "testdb" in dblist:
    print("数据库已存在！")

# 验证集合是否存在
collist = mydb.list_collection_names()
# collist = mydb.collection_names()
if "sites" in collist:  # 判断 sites 集合是否存在
    print("集合已存在！")
