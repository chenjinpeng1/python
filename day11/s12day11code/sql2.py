#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine,and_,or_,func,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,ForeignKey
from  sqlalchemy.orm import sessionmaker,relationship

Base = declarative_base() #生成一个SqlORM 基类


Host2Group = Table('host_2_group',Base.metadata,
    Column('host_id',ForeignKey('host.id'),primary_key=True),
    Column('group_id',ForeignKey('group.id'),primary_key=True),
)




engine = create_engine("mysql+mysqldb://root:123@localhost:3306/test",echo=True)


class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer,primary_key=True,autoincrement=True)
    hostname = Column(String(64),unique=True,nullable=False)
    ip_addr = Column(String(128),unique=True,nullable=False)
    port = Column(Integer,default=22)
    #group_id = Column(Integer, ForeignKey('group.id'))
    groups = relationship('Group',
                          secondary=Host2Group,
                          backref='host_list')

    #group =relationship("Group",backref='host_list')
    #group =relationship("Group",back_populates='host_list')
    def __repr__(self):
        return  "<id=%s,hostname=%s, ip_addr=%s>" %(self.id,
                                                    self.hostname,
                                                    self.ip_addr)
class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer,primary_key=True)
    name = Column(String(64),unique=True,nullable=False)
    #host_id = Column(Integer,ForeignKey('hosts.id'))
    #host_list =relationship("Host", back_populates="group")
    #hosts =relationship("Host")
    def __repr__(self):
        return  "<id=%s,name=%s>" %(self.id,self.name)

Base.metadata.create_all(engine) #创建所有表结构

if __name__ == '__main__':
    SessionCls = sessionmaker(bind=engine) #创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
    session = SessionCls() #连接的实例
    #h1 = Host(hostname='localhost',ip_addr='127.0.0.1')
    #h2 = Host(hostname='ubuntu',ip_addr='192.168.1.55',port=10000)
    #session.add(h1)
    #session.add(h2)
    #session.add_all([h1,h2])
    #update
    #obj = session.query(Host).filter(Host.hostname=="test server").first()
    #session.query(Host).filter(Host.port.)

    #print("++>",obj)
    #obj.hostname = "test server"
    #session.delete(obj)
    #objs = session.query(Host).filter(and_(Host.hostname.like("ub%"), Host.port > 20)).all()
    #print("-->",objs)

    #FK
    '''
    g1 = Group(name='g1')
    g2 = Group(name='g2')
    g3 = Group(name='g3')
    g4= Group(name='g4')
    session.add_all([g1,g2,g3,g4])
    '''
    #session.add_all([g4,])
    #g4 = session.query(Group).filter(Group.name=='g4').first()
    #h = session.query(Host).filter(Host.hostname=='localhost').update({'group_id':g4.id})
    #h = session.query(Host).filter(Host.hostname=='localhost').first()
    #print("h1:",h.group.name )
    #print("g:",g4.host_list )
    #h1 = Host(hostname='localhost',ip_addr='127.0.0.1',group_id=g4.id)
    #h2 = Host(hostname='ubuntu',ip_addr='192.168.1.55',port=10000,group_id=g4.id)

    #session.add(h2)
    '''
    h1 = Host(hostname='h1',ip_addr='192.168.1.56')
    h2 = Host(hostname='h2',ip_addr='192.168.1.57',port=10000)
    h3 = Host(hostname='ubuntu',ip_addr='192.168.1.58',port=10000)
    session.add_all([h1,h2,h3])
    '''
    #groups = session.query(Group).all()
    g1 = session.query(Group).first()

    h2 = session.query(Host).filter(Host.hostname=='h2').first()
    #h2.groups = groups[1:-1]
    print("===========>",h2.groups)
    print("===========g1>",g1.host_list)
    #h1.groups.pop()
    # join select
    #objs = #session.query(Host).join(Host.group).group_by(Group.name).all()
    #objs = session.query(Host,func.count(Group.name)).\
    #    join(Host.group).group_by(Group.name).all()

    #print("-->objs:",objs)
    session.commit()