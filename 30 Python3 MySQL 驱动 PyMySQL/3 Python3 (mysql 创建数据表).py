import pymysql

# 打开数据库连接
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='pass',
                     database='runoob_db')  # 数据库

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 1.创建数据库表
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)
db.close()
