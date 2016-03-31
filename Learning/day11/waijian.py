import pymysql
from sqlalchemy import create_engine,MetaData,ForeignKey,and_,or_,func,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from  sqlalchemy.orm import sessionmaker,relationship,backref#反向关联模块
# 生成一个sqlorm基类
Base = declarative_base()
#创建一个引擎
engine = create_engine("mysql+pymysql://root:chen27@localhost:3306/chen",echo=True)

# 多对多
# 创建另一个表 与hosts和groups表相关联
Hosts_2_Groups = Table('Hosts_2_Groups',Base.metadata,
    # Column('id',nullable=False,autoincrement=True),
    Column('host_id',ForeignKey('hosts.id'),primary_key=True),
    Column('group_id',ForeignKey('groups.id'),primary_key=True),
)
class Hosts(Base):
    __tablename__='hosts'
    id = Column(Integer,primary_key=True)
    hostname = Column(String(64),unique=True,nullable=False)
    ip_addr = Column(String(128),unique=True,nullable=False)
    port = Column(Integer,default=22)
    group = relationship("Groups",backref="hosts_list",secondary=Hosts_2_Groups) #secondary指定中间表的实例
    def __repr__(self): # 返回一些信息
        return "<id=%s,hostname=%s,ip_addr=%s>" %(self.id,
                                                  self.hostname,
                                                  self.ip_addr)
class Groups(Base):
    __tablename__='groups'
    id = Column(Integer,primary_key=True)
    groupname = Column(String(64),unique=True,nullable=False)
    # hosts = relationship("Hosts")
    def __repr__(self):
        return "id=%s,groupname=%s"%(self.id,self.groupname)
Base.metadata.create_all(engine)

if __name__ == "__main__":
    sess = sessionmaker(bind=engine)
    session = sess()
    g1 = Groups(groupname = "g1")
    g2 = Groups(groupname = "g2")
    g3 = Groups(groupname = "g3")
    g4 = Groups(groupname = "g4")
    h1 = Hosts(hostname="h1",ip_addr="192.168.1.10")
    h2 = Hosts(hostname="h2",ip_addr="192.168.1.11")
    h3 = Hosts(hostname="h3",ip_addr="192.168.1.12")
    # #
    # session.add_all([h1,h2,h3,g1,g2,g3,g4])
    # session.commit()
    # h1 = session.query(Hosts).filter(Hosts.hostname=="h2").first()
    # groups = session.query(Groups).all()
    # h1.group= groups
    # session.commit()
    # print(h2.group)
    # g2 = session.query(Groups).filter(Groups.groupname=="g2").first()
    # print(g2.hosts_list)

    # h1 = session.query(Hosts).filter(Hosts.hostname=="h1").first()
    # print(h1.group)
    # h3 = Hosts(hostname="h3",ip_addr="192.168.1.12",group_id="1")
    # session.add(h3)
    # session.commit()
    # g1 = session.query(Groups).filter(Groups.groupname=="g1").first()
    # for i in g1.hosts_list:print(i.hostname)
    #[<__main__.Hosts object at 0x7ffb945af5f8>, <__main__.Hosts object at 0x7ffb945af668>]
    #inner join
    # ret = session.query(Hosts).join(Hosts.group).filter(Groups.groupname=="g1").all()
    # for i in ret:print(i.hostname)
    # ret = session.query(Hosts,func.count(Groups.groupname)).join(Hosts.group).group_by(Groups.groupname).all()
    # print(ret)
