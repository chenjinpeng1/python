import pymysql
from sqlalchemy import create_engine,MetaData,ForeignKey,and_,or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from  sqlalchemy.orm import sessionmaker,relationship,backref#反向关联模块
# 生成一个sqlorm基类
Base = declarative_base()
#创建一个引擎
engine = create_engine("mysql+pymysql://root:chen27@localhost:3306/chen",echo=True)

class Hosts(Base):
    __tablename__='hosts'
    id = Column(Integer,primary_key=True)
    hostname = Column(String(64),unique=True,nullable=False)
    ip_addr = Column(String(128),unique=True,nullable=False)
    port = Column(Integer,default=22)
    group_id = Column(Integer,ForeignKey('groups.id')) # 外键关联groups下的id
    group = relationship("Groups",backref='hosts_list') # backref表示反向关联hosts_list可以指定任意字符串，但是你调用的时候必须一致
class Groups(Base):
    __tablename__='groups'
    id = Column(Integer,primary_key=True)
    groupname = Column(String(64),unique=True,nullable=False)
    # hosts = relationship("Hosts")
Base.metadata.create_all(engine)

if __name__ == "__main__":
    sess = sessionmaker(bind=engine)
    session = sess()
    # g1 = Groups(groupname = "g1")
    # g2 = Groups(groupname = "g2")
    # g3 = Groups(groupname = "g3")
    # h1 = Hosts(hostname="h1",ip_addr="192.168.1.10",group_id="1")
    # h2 = Hosts(hostname="h2",ip_addr="192.168.1.11",group_id="2")
    #
    # session.add_all([h1,h2,g1,g2,g3])
    # session.commit()
    # h1 = session.query(Hosts).filter(Hosts.hostname=="h1").first()
    # print(h1.group.groupname)
    # h3 = Hosts(hostname="h3",ip_addr="192.168.1.12",group_id="1")
    # session.add(h3)
    # session.commit()
    # g1 = session.query(Groups).filter(Groups.groupname=="g1").first()
    # print(g1.hosts_list)
    #[<__main__.Hosts object at 0x7ffb945af5f8>, <__main__.Hosts object at 0x7ffb945af668>]
    #inner join
    # ret = session.query(Hosts).join(Hosts.group).filter(Hosts.group_id=="1").group_by(Groups.groupname=="g1").all()
    ret = session.query(Hosts).join(Hosts.group).filter(Groups.groupname=="g1").all()
    print(ret)
    print(len(ret))
