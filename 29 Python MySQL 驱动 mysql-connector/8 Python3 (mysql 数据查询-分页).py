import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",  # 数据库主机地址
    port="3306",  # 数据库端口
    user="root",  # 数据库用户名
    passwd="pass",  # 数据库密码
    database="runoob_db"  # 先确定数据库已经存在
)
mycursor = mydb.cursor()

# 分页查询 limit
mycursor.execute("SELECT * FROM sites LIMIT 3")
# 也可以指定起始位置，使用的关键字是 OFFSET
# mycursor.execute("SELECT * FROM sites LIMIT 3 OFFSET 1")  # 0 为 第一条，1 为第二条，以此类推
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

