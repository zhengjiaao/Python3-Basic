import pymysql

# 打开数据库连接
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='pass',
                     database='runoob_db')  # 数据库

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

# 也可以这样写 SQL 插入语句
# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#        LAST_NAME, AGE, SEX, INCOME) \
#        VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
#        ('Mac', 'Mohan', 20, 'M', 2000)

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()


