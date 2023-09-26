import pymongo

# 1.有密码连接，有认证
myclient = pymongo.MongoClient("mongodb://myUserTest:123456@localhost:27017/admin")  # admin 是认证数据库

mydb = myclient["testdb"]  # 数据库
mycol = mydb["sites"]  # 集合

# 2. 修改一条文档 update_one()
# 在 MongoDB 中使用 update_one() 方法修改文档中的记录。该方法第一个参数为查询的条件，第二个参数为要修改的字段。
# 如果查找到的匹配数据多于一条，则只会修改第一条。
myquery = {"alexa": "10000"}
newvalues = {"$set": {"alexa": "12345"}}
mycol.update_one(myquery, newvalues)
# 输出修改后的  "sites"  集合
for x in mycol.find():
    print(x)

# {'_id': ObjectId('6507b12c9d51a92839d1620a'), 'name': 'RUNOOB', 'alexa': '12345', 'url': 'https://www.runoob.com'}
# {'_id': ObjectId('6507baf2c481cc80bf366324'), 'name': 'RUNOOB', 'alexa': '10000', 'url': 'https://www.runoob.com'}
# {'_id': ObjectId('6507bb47b3619adfe19955ac'), 'name': 'RUNOOB', 'alexa': '10000', 'url': 'https://www.runoob.com'}
# {'_id': ObjectId('6507bb47b3619adfe19955ad'), 'name': 'Taobao', 'alexa': '100', 'url': 'https://www.taobao.com'}

print('\n')

# 3. 修改所有匹配到的记录 update_many()
myquery = {"name": {"$regex": "^F"}}
newvalues = {"$set": {"alexa": "123"}}

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "文档已修改")

# 输出修改后的  "sites"  集合
for x in mycol.find():
    print(x)
