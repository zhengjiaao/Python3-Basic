import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",  # 数据库主机地址
    port="3306",  # 数据库端口
    user="root",  # 数据库用户名
    passwd="pass",  # 数据库密码
    database="runoob_db"  # 先确定数据库已经存在
)
mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites

mycursor.execute(sql)
