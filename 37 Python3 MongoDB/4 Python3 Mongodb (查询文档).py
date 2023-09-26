# MongoDB 中使用了 find 和 find_one 方法来查询集合中的数据，它类似于 SQL 中的 SELECT 语句。

import pymongo

# 1.有密码连接，有认证
myclient = pymongo.MongoClient("mongodb://myUserTest:123456@localhost:27017/admin")  # admin 是认证数据库

mydb = myclient["testdb"]  # 数据库
mycol = mydb["sites"]  # 集合

# 2.查询一条数据 find_one()
x = mycol.find_one()
print(x)
# {'_id': ObjectId('6507b12c9d51a92839d1620a'), 'name': 'RUNOOB', 'alexa': '10000', 'url': 'https://www.runoob.com'}

print('\n')

# 3.查询集合中所有数据 find(),类似 SQL 中的 SELECT * 操作。
for x in mycol.find():
    print(x)

print('\n')

# 4.查询指定字段的数据 find() ，将要返回的字段对应值设置为 1。
# 除了 _id，你不能在一个对象中同时指定 0 和 1，如果你设置了一个字段为 0，则其他都为 1，反之亦然。
for x in mycol.find({}, {"_id": 0, "name": 1, "alexa": 1}):
    print(x)

# 会报错，除了_id,其他字段不能同时设置 0 和 1
# for x in mycol.find({},{ "name": 1, "alexa": 0 }):

print('\n')

# 5.根据指定条件查询
myquery = {"name": "RUNOOB"}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

print('\n')

# 6. 高级查询
myquery = {"name": {"$gt": "H"}}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

# 6.使用正则表达式查询
myquery = {"name": {"$regex": "^R"}}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

# 7.返回指定条数记录
myresult = mycol.find().limit(3)
# 输出结果
for x in myresult:
    print(x)
