import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from  sqlalchemy.orm import sessionmaker
# 生成一个sqlorm基类
Base = declarative_base()
#创建一个引擎
engine = create_engine("mysql+pymhsql://root:chen27@localhost:3306/chen",echo=False)

#创建表
class Host(Base):
    __tablename__='hosts' # 表名
    id = Column(Integer,primary_key=True,autoincrement=True) #（整数型，主键，自增）
    hostname = Column(String(64),unique=True,nullable=False) #(字符串，唯一性，不能为空)
    ip_addr=Column(String(128),unique=True,nullable=False)
    port = Column(Integer,default=22) # default 设置默认值

class Groups(Base):
    __tablename__='groups'
