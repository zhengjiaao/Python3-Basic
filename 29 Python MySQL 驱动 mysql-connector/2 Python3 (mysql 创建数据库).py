import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",  # 数据库主机地址
    port="3306",  # 数据库端口
    user="root",  # 数据库用户名
    passwd="pass"  # 数据库密码
)

print(mydb)

mycursor = mydb.cursor()

# 1.创建一个名为 runoob_db 的数据库
mycursor.execute("CREATE DATABASE runoob_db")

# 2.校验数据库存在
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

# 3. 或者我们可以直接连接数据库，如果数据库不存在，会输出错误信息
mydb = mysql.connector.connect(
    host="127.0.0.1",  # 数据库主机地址
    port="3306",  # 数据库端口
    user="root",  # 数据库用户名
    passwd="pass",  # 数据库密码
    database="runoob_db"
)
