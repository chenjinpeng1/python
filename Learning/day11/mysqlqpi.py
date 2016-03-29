import pymysql
from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from  sqlalchemy.orm import sessionmaker
# 生成一个sqlorm基类
Base = declarative_base()
#创建一个引擎
engine = create_engine("mysql+pymysql://root:chen27@localhost:3306/chen",echo=False)

#创建表
class Host(Base):
    __tablename__='hosts' # 表名
    id = Column(Integer,primary_key=True,autoincrement=True) #（整数型，主键，自增）
    hostname = Column(String(64),unique=True,nullable=False) #(字符串，唯一性，不能为空)
    ip_addr=Column(String(128),unique=True,nullable=False)
    port = Column(Integer,default=22) # default 设置默认值
class Groups(Base):
    __tablename__='groups'
    id = Column(Integer,primary_key=True,autoincrement=True)
    groupname = Column(String(128),unique=True,nullable=False)
class Users(Base):
    __tablename__='users'
    id = Column(Integer,primary_key=True,autoincrement=True) #（整数型，主键，自增）
    username =Column(String(64),unique=True,nullable=False)
    passwd = Column(String(128))
    groupname = Column(String(128),nullable=False)
Base.metadata.create_all(engine)
if __name__ == '__main__':
    SessionCLs = sessionmaker(bind=engine)
    session = SessionCLs()
    u1 = Users(username = 'chen',passwd='chen27',groupname='g1')
    u2 = Users(username = 'qiu',passwd='chen27',groupname='g2')
    # h1 = Host(hostname = 'localhost',ip_addr='127.0.0.1')
    # h2 = Host(hostname = 'ubuntu',ip_addr='localhost',port = 22)
    # g1 = Groups(groupname='g1')
    # g2 = Groups(groupname = 'g2')
    session.add_all([u1,u2])
    session.commit()
    # res = session.query(Host).filter(Host.hostname=="localhost").update({'hostname':'ubuntu'})
    # session.commit()
    # print(res)
    # for i in res:print(i.ip_addr,i.port)
