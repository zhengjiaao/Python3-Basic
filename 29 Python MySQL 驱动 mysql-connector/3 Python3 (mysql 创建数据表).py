import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",  # 数据库主机地址
    port="3306",  # 数据库端口
    user="root",  # 数据库用户名
    passwd="pass",  # 数据库密码
    database="runoob_db"  # 先确定数据库已经存在
)

print(mydb)

mycursor = mydb.cursor()

# 1.删除表，如果存在表就给删除掉
sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites
mycursor.execute(sql)

# 2. 创建表
mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")
# or 直接在创建表时设置主键
# mycursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")

# 3. 查看数据表是否已存在
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

# 4. 给表设置主键(前提是表已存在)
mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
