import mysql.connector

# 注意：UPDATE 语句要确保指定了 WHERE 条件语句，否则会导致整表数据被更新。

mydb = mysql.connector.connect(
    host="127.0.0.1",  # 数据库主机地址
    port="3306",  # 数据库端口
    user="root",  # 数据库用户名
    passwd="pass",  # 数据库密码
    database="runoob_db"  # 先确定数据库已经存在
)
mycursor = mydb.cursor()

# 1. 更新数据
sql = "UPDATE sites SET name = 'ZH' WHERE name = 'Zhihu'"

mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, " 条记录被修改")  # 1  条记录被修改

# 2. 更新数据
# 为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义更新语句的条件
sql = "UPDATE sites SET name = %s WHERE name = %s"
val = ("Zhihu", "ZH")

mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, " 条记录被修改")
