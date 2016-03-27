from sqlalchemy import create_engine,ForeignKey,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from  sqlalchemy.orm import sessionmaker,relationship


Base = declarative_base() # 生成一个sqlorm基类,Base不是一个实例，是一个类
engine = create_engine("mysql+pymysql://root:chen27@localhost:3306/chen",echo=False)
Host2Group = Table('host_2_group',Base.metadata,
                   Column('host_id',ForeignKey('hosts.id'),primary_key=True),
                   Column('group_id',ForeignKey('groups.id'),primary_key=True))
class Host(Base):
    __tablename__ = 'hosts' # 定义表名
    id = Column(Integer,primary_key=True,autoincrement=True) # intger 整数型,primary_key主键,autoincrement自动增量d
    hostname = Column(String(64),unique=True,nullable=False) # unique表示唯一性,nullable=False表示不能为空
    ip_addr = Column(String(128),unique=True,nullable=False)
    port = Column(Integer,default=22) #default=22 默认为22
    # group_id=Column(Integer)
    groups = relationship('Group',
                          secondary=Host2Group,
                          backref='host_list')

# Base.metadata.create_all(engine)# 创建表结构,如果表存在，报错
class Groups(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(64),unique=True,nullable=False)
Base.metadata.create_all(engine)# 创建表结构,如果表存在，报错

if __name__=='__main__':
    SessionCls=sessionmaker(bind=engine)#创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
    Session = SessionCls()# 实例化类
    h1 = Host(hostname="localhost",ip_addr='127.0.0.1',group_id="g1")
    h2 = Host(hostname="ubuntu",ip_addr='192.168.2.243',port=20000,group_id="g1")
    h3 = Host(hostname='ubuntu2',ip_addr='192.168.2.244',port=20000,group_id="g2")
    g1 = Groups(name="g1")
    g2 = Groups(name="g2")
    # h3.hostname="centos"# 只要没有commit 随时可以修改数据
    Session.add_all([h1,h2,h3,g1,g2]) # add_all 全部添加
    g1 = Session.query(Groups).first()
    h2 = Session.query(Host).filter(Host.hostname=="h2").first()
    print("=====",h2.groups)
    print("---",g1.host_list)
    Session.commit() # 提交
    # res = Session.query(Host).filter(Host.hostname.in_(['ubuntu','localhost'])).all()
    # Session.commit()
    # print(res)
