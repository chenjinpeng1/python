import pymysql
from sqlalchemy import create_engine,MetaData,ForeignKey,and_,or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from  sqlalchemy.orm import sessionmaker,relationship
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
    # groupid = Column(String(64),ForeignKey("groups.groupid"))
    port = Column(Integer,default=22) # default 设置默认值
class Groups(Base):
    __tablename__='groups'
    id = Column(Integer,primary_key=True,autoincrement=True)
    groupid = Column(String(64))
    groupname = Column(String(128),unique=True,nullable=False)
    # host_ip_fk=relationship("hosts")
# class Users(Base):
#     __tablename__='users'
#     id = Column(Integer,primary_key=True,autoincrement=True) #（整数型，主键，自增）
#     userid = Column(String(128))
#     username =Column(String(64),unique=True,nullable=False)
#     passwd = Column(String(128))
#     groupname = Column(String(128),nullable=False)
#     host_ip_fk=relationship("groups")
Base.metadata.create_all(engine) # 创建表。如果存在 则忽略
if __name__ == '__main__':
    SessionCLs = sessionmaker(bind=engine)#创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
    session = SessionCLs()
    # u1 = Users(username = 'chen',passwd='chen27',groupname='g1')
    # u2 = Users(username = 'qiu',passwd='chen27',groupname='g2')
    # h1 = Host(hostname = 'localhost',ip_addr='127.0.0.1')
    # h2 = Host(hostname = 'ubuntu',ip_addr='localhost',port = 22)
    # g1 = Groups(groupname='g1')
    # g2 = Groups(groupname = 'g2')
    # session.add_all([h1,h2,g1,g2])
    # session.commit()
    # res = session.query(Host).filter(Host.hostname=="ubuntu").first()
    # print(res.hostname)
    # session.delete(res)
    # session.commit()
    # print(res)
    # for i in res:print(i.ip_addr,i.port)
    #增加
    # u = Users(username="alex",passwd="123",groupname="g1")
    # session.add(u)
    # session.add_all([Users(username="sb1",passwd="123",groupname="g2"),
    #                  Users(username="sb2",passwd="123",groupname="g2")])
    # session.commit()
    # h3 = Host(hostname ="linux",ip_addr="192.168.1.10")
    # session.add(h3)
    # session.commit()
    # session.add_all([
    #     Host(hostname="aa",ip_addr="192.168.1.11"),
    #     Host(hostname="bb",ip_addr="192.168.1.12")]
    # )
    # session.commit()
    # #删除
    # session.query(Host).filter(Host.id >4).delete()
    # session.commit()
    # session.query(Users).filter(Users.id>4).delete()
    # session.commit()
    #修改
    # session.query(Users).filter(Users.id == 4).update({"groupname":"g1"})
    # session.commit()
    #查询
    # ret = session.query(Host).filter(and_(Host.hostname.like("ub%"),Host.port >20)).all()
    # for i in ret:print(i.hostname)
    # ret = session.query(Host).filter(Host.hostname.match("ubuntu"))
    # print(ret)
    # for i in ret:print(i.hostname)
    # ret=session.query(Users).filter(Users.id > 2).first()
    # print(ret.groupname)#指定为first显示为这样显示
    # ret=session.query(Users).filter(Users.id > 2).all()
    # for i in ret:print(i.groupname) # 指定为返回的是一个列表，列表里包含类
    # ret=session.query(Users).filter_by(groupname="g1").all()#过滤器类型为filter_by时,可以过滤一些关键字
    # print(ret.groupname)#
    # for i in ret:print(i.groupname)
    # ret = session.query(Users).filter(Users.groupname.in_(["g1","g2"])).all()#.in_表示包含在后面的列表里的值
    # for i in ret:print(i.groupname)
    # ret = session.query(Users.groupname.label("wocao")).all()#label表示将表中的字段起一个别名
    # print (ret,type(ret))
    # ret = session.query(Users).order_by(Users.groupname).all()# order_by 排序，在此表示对Users下的groupname字段排序
    # for i in ret:print(i.groupname)
    # ret = session.query(Users).filter(Users.id > 1).order_by(Users.groupname).all()#order_by 排序，在此表示对Users下的id字段大于2的groupname排序
    # for i in ret:print(i.groupname)
    # ret = session.query(Users).filter(Users.id > 1).order_by(Users.groupname)[1:3]#order_by 排序，在此表示对Users下的id字段大于2的groupname排序,进行切片操作，获取第1个和第2个的值
    # for i in ret:print(i.groupname)

    #外键关联
