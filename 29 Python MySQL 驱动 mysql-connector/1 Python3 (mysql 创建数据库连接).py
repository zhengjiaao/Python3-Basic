import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",  # 数据库主机地址
    port="3306",  # 数据库端口
    user="root",  # 数据库用户名
    passwd="pass"  # 数据库密码
)

print(mydb)
