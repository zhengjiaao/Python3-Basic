import pymongo

# 1.有密码连接，有认证
myclient = pymongo.MongoClient("mongodb://myUserTest:123456@localhost:27017/admin")  # admin 是认证数据库

mydb = myclient["testdb"]  # 数据库
mycol = mydb["sites"]  # 集合

# 2. 对字段 alexa 按升序排序
# sort() 方法可以指定升序或降序排序。
# sort() 方法第一个参数为要排序的字段，第二个字段指定排序规则，1 为升序，-1 为降序，默认为升序。
mydoc = mycol.find().sort("alexa")
for x in mydoc:
    print(x)

print('\n')

# 3. 对字段 alexa 按降序排序
mydoc = mycol.find().sort("alexa", -1)
for x in mydoc:
    print(x)
