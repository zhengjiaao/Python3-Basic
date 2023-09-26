import pymysql

# 打开数据库连接
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='pass',
                     database='runoob_db')  # 数据库

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 1. 将表中的 SEX 为 'M' 的 AGE 字段递增 1
# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()
