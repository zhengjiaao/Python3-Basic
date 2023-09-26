import pymysql

# 打开数据库连接
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='pass')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 1.创建一个名为 runoob_db 的数据库
sql = "CREATE DATABASE runoob_db"

cursor.execute(sql)
db.close()
