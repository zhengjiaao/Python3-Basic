# Python MongoDB

**PyMongo**

Python 要连接 MongoDB 需要 MongoDB 驱动，这里我们使用 PyMongo 驱动来连接。

## 安装 PyMongo

```shell
python3 -m pip3 install pymongo
# or 指定安装的版本
python3 -m pip3 install pymongo==3.5.1
# or 更新
python3 -m pip3 install --upgrade pymongo
```

## 测试

> 创建一个数据库

```python
#!/usr/bin/python3

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# 创建数据库 runoobdb
mydb = myclient["runoobdb"]

# 检验是否存在
dblist = myclient.list_database_names()
# dblist = myclient.database_names() 
if "runoobdb" in dblist:
    print("数据库已存在！")
```

