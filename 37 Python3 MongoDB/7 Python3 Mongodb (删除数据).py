import pymongo

# 1.有密码连接，有认证
myclient = pymongo.MongoClient("mongodb://myUserTest:123456@localhost:27017/admin")  # admin 是认证数据库

mydb = myclient["testdb"]  # 数据库
mycol = mydb["sites"]  # 集合

# 1. 删除 name 字段值为 "Taobao" 的文档
# delete_one() 方法来删除一个文档，该方法第一个参数为查询对象，指定要删除哪些数据。

myquery = {"name": "Taobao"}
mycol.delete_one(myquery)

# 删除后输出
for x in mycol.find():
    print(x)

# 2. 删除所有 name 字段中以 F 开头的文档，删除多个文档
# delete_many() 方法来删除多个文档，该方法第一个参数为查询对象，指定要删除哪些数据。
myquery = {"name": {"$regex": "^F"}}

x = mycol.delete_many(myquery)

print(x.deleted_count, "个文档已删除")  # 1 个文档已删除

# 3. 删除集合中的所有文档
# delete_many() 方法如果传入的是一个空的查询对象，则会删除集合中的所有文档
x = mycol.delete_many({})

print(x.deleted_count, "个文档已删除")  # 5 个文档已删除

# 4.删除集合
# drop() 方法来删除一个集合。

mycol = mydb["sites"]
mycol.drop()
