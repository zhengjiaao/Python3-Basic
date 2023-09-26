# Python MySQL - mysql-connector 驱动

使用 mysql-connector 来连接使用 MySQL， mysql-connector 是 MySQL 官方提供的驱动器。


## 安装
```python
python -m pip install mysql-connector
```

## 测试

```python
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="yourusername",  # 数据库用户名
    passwd="yourpassword"  # 数据库密码
)

print(mydb)
```