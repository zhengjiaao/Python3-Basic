import pymysql

# 打开数据库连接
db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='pass',
                     database='runoob_db')  # 数据库

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 1. 删除数据表 EMPLOYEE 中 AGE 大于 20 的所有数据
# SQL 删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交修改
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭连接
db.close()
