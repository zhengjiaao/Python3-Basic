import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",  # 数据库主机地址
    port="3306",  # 数据库端口
    user="root",  # 数据库用户名
    passwd="pass",  # 数据库密码
    database="runoob_db"  # 先确定数据库已经存在
)
mycursor = mydb.cursor()

# 1. 查询数据(全部)
mycursor.execute("SELECT * FROM sites")
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
for x in myresult:
    print(x)

print('\n ---------分隔符----------\n')

# 2. 查询指定的字段数据
mycursor.execute("SELECT name, url FROM sites")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print('\n ---------分隔符----------\n')

# 3. 查询一条数据
# 使用 fetchone() 方法
mycursor.execute("SELECT * FROM sites")
myresult = mycursor.fetchone()
print(myresult)