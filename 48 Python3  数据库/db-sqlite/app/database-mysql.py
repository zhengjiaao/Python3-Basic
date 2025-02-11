from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 修改为 MySQL 连接字符串
SQLALCHEMY_DATABASE_URL = "db-mysql+pymysql://test:pass@localhost/test"

# 创建 MySQL 引擎
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建基类
Base = declarative_base()
