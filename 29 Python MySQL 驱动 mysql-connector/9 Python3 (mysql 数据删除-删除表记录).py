import mysql.connector

# 注意：要慎重使用删除语句，删除语句要确保指定了 WHERE 条件语句，否则会导致整表数据被删除。

mydb = mysql.connector.connect(
    host="127.0.0.1",  # 数据库主机地址
    port="3306",  # 数据库端口
    user="root",  # 数据库用户名
    passwd="pass",  # 数据库密码
    database="runoob_db"  # 先确定数据库已经存在
)
mycursor = mydb.cursor()

# 1. 删除表某条记录
sql = "DELETE FROM sites WHERE name = 'stackoverflow'"

mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, " 条记录删除")

# 1  条记录删除

# 2. 删除表某条记录
# 为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义删除语句的条件

sql = "DELETE FROM sites WHERE name = %s"
na = ("stackoverflow",)

mycursor.execute(sql, na)
mydb.commit()
print(mycursor.rowcount, " 条记录删除") # 如果记录不存在，则删除0条记录

# 0  条记录删除