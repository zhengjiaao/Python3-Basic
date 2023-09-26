import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",  # 数据库主机地址
    port="3306",  # 数据库端口
    user="root",  # 数据库用户名
    passwd="pass",  # 数据库密码
    database="runoob_db"  # 先确定数据库已经存在
)
mycursor = mydb.cursor()

# 1. 查询指定条件的数据
# 使用 where 条件语句
sql = "SELECT * FROM sites WHERE name ='RUNOOB'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print('\n ---------分隔符----------\n')

# 1.2 查询指定条件的数据
# 使用 where 条件语句
# 防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义查询的条件

sql = "SELECT * FROM sites WHERE name = %s"
na = ("RUNOOB",)
mycursor.execute(sql, na)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print('\n ---------分隔符----------\n')

# 1.2 查询指定条件的数据
# 使用 where 条件语句
# 也可以使用通配符 %
sql = "SELECT * FROM sites WHERE url LIKE '%oo%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print('\n ---------分隔符----------\n')
