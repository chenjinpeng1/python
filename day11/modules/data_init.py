import pymysql
from sqlalchemy import create_engine,MetaData,ForeignKey,and_,or_,func,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,UniqueConstraint
from  sqlalchemy.orm import sessionmaker,relationship,backref#反向关联模块
# 生成一个sqlorm基类
Base = declarative_base()
engine = create_engine("mysql+pymysql://root:chen27@localhost:3306/chen",echo=True)

# Hosts_2_Groups = Table('Hosts_2_Groups',Base.metadata,
#     # Column('id',nullable=False,autoincrement=True),
#     Column('host_id',ForeignKey('hosts.id'),primary_key=True),
#     Column('group_id',ForeignKey('groups.id'),primary_key=True),
# )
Userprofile_group = Table("Userprofile_group",Base.metadata,
    Column("userprofile_id",ForeignKey("userprofiles.id"),primary_key=True),
    Column("group_id",ForeignKey("groups.id"),primary_key=True))

Userprofile_hostuser = Table("Userprofile_hostuser",Base.metadata,
    Column("userprofile_id",ForeignKey("userprofiles.id"),primary_key=True),
    Column("hostuser_id",ForeignKey("hostusers.id"),primary_key=True))

Hostuser_group = Table("Hostuser_group",Base.metadata,
    Column("hostuser_id",ForeignKey("hostusers.id"),primary_key=True),
    Column("group_id",ForeignKey("groups.id"),primary_key=True))
class Hosts(Base):
    __tablename__='hosts'
    id = Column(Integer,primary_key=True,autoincrement=True)
    hostname = Column(String(64),unique=True,nullable=False)
    address = Column(String(128),unique=True,nullable=False)
    port = Column(Integer,default=22)
    # group = relationship("Groups",backref="hosts_list",secondary=Hosts_2_Groups) #secondary指定中间表的实例
    def __repr__(self): # 返回一些信息
        return "<id=%s,hostname=%s,address=%s,port=%s>" %(self.id,
                                                  self.hostname,
                                                  self.address,
                                                  self.port)
class Groups(Base):
    __tablename__='groups'
    id = Column(Integer,primary_key=True,autoincrement=True)
    groupname = Column(String(64),unique=True,nullable=False)
    # hosts = relationship("Hosts")
    def __repr__(self):
        return "id=%s,groupname=%s"%(self.id,self.groupname)

class Userprofiles(Base):
    __tablename__='userprofiles'
    id = Column(Integer,primary_key=True,autoincrement=True)
    user = Column(String(64),nullable=False,unique=True)
    passwd = Column(String(64),nullable=False)
    group = relationship("Groups",backref="userprofiles",secondary=Userprofile_group)
    hostuser = relationship("Hostusers",backref="userprofiles",secondary=Userprofile_hostuser)
    def __repr__(self):
        return "id=%s,user=%s"%(self.id,self.user)
    # __table_args__ = (UniqueConstraint( 'id', 'user',name='_host_username_uc'),)

class Hostusers(Base):
    __tablename__='hostusers'
    id = Column(Integer,primary_key=True)
    hostid = Column(Integer,ForeignKey("hosts.id"))
    user = Column(String(64),nullable=False)
    passwd = Column(String(64))
    group = relationship("Groups",backref="hostusers",secondary=Hostuser_group)
    def __repr__(self):
        return "id=%s,user=%s"%(self.id,self.user)
    __table_args__ = (UniqueConstraint( 'hostid','user', name='_host_username_uc'),)#联合唯一

# sess = sessionmaker(bind=engine)
# session = sess()
# userprofile_2_group = session.query(Userprofiles).filter(Userprofiles.user=="chen").first()
# group = session.query(Groups).filter(Groups.groupname=="webserver").first()
# print(group.id)
# userprofile_2_group.group=[group]
# session.commit()
# userprofile_2_user = session.query(Userprofiles).filter(Userprofiles.user=="chen").first()
# user = session.query(Hostusers).filter(Hostusers.user=="chen").first()
# userprofile_2_user.hostuser = [user]
# session.commit()
# userprofile_2_user = session.query(Userprofiles).filter(Userprofiles.user=="chen").first()
# user = session.query(Hostusers).filter(Hostusers.user=="test").first()
# userprofile_2_user.hostuser = [user]
# session.commit()
