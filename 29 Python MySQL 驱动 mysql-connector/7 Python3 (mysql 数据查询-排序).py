import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",  # 数据库主机地址
    port="3306",  # 数据库端口
    user="root",  # 数据库用户名
    passwd="pass",  # 数据库密码
    database="runoob_db"  # 先确定数据库已经存在
)
mycursor = mydb.cursor()

# 1. 排序
# 查询结果排序可以使用 ORDER BY 语句，默认的排序方式为升序，关键字为 ASC，如果要设置降序排序，可以设置关键字 DESC
# 默认 升序
sql = "SELECT * FROM sites ORDER BY name"
# 降序
# sql = "SELECT * FROM sites ORDER BY name DESC"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
