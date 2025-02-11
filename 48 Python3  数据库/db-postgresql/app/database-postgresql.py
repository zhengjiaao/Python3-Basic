from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 修改为 PostgreSQL 连接字符串
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://test:pass@localhost:5432/test?options=-csearch_path=public"  # 确保端口正确

# 创建 PostgreSQL 引擎
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # echo=True  # 可选：启用 SQL 日志
)

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建基类
Base = declarative_base()
