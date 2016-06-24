import sys,os
Base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import yaml
from sqlalchemy.ext.declarative import declarative_base
from modules.mysql_conn import engine,session
from modules import data_init
from  sqlalchemy.orm import sessionmaker,relationship,backref#反向关联模块




def createhost(argv):
    if "-f" in argv:
        file = argv[argv.index("-f")+1]
        filename="%s/%s/%s"%(Base,"conf",file)
        f = open(filename,"r")
        info = yaml.load(f)
        for key,val in info.items():
            from modules.data_init import Hosts
            print(key,info[key]["ipaddress"],info[key]["port"])
            # for i in val:
            u1 = Hosts(hostname=key,address=info[key]["ipaddress"],port=info[key]["port"])
            session.add(u1)
            session.commit()
    else:
        print('''
        -f 指定配置文件
        ''')
def createuser(argv):
    if "-f" in argv:
        file = argv[argv.index("-f")+1]
        filename="%s/%s/%s"%(Base,"conf",file)
        f = open(filename,"r")
        info = yaml.load(f)
        for key,val in info.items():
            u = key
            p = info[u]["password"]
            from modules.data_init import Userprofiles
            u1 = Userprofiles(user=u,passwd=p)
            session.add(u1)
            session.commit()
    else:
        print('''
        -f 指定配置文件
        ''')

def initdb(argv):
    print("init db")
    data_init.Base.metadata.create_all(engine)

def creategroup(argv):
    if "-f" in argv:
        file = argv[argv.index("-f")+1]
        filename="%s/%s/%s"%(Base,"conf",file)
        f = open(filename,"r")
        info = yaml.load(f)
        for key,val in info.items():
            # print(key)
            # print(val)
            for i in val:
                from modules.data_init import Groups
                # for i in key:
                g1 = Groups(groupname=i)
                session.add(g1)
                session.commit()
    else:
        print('''
        -f 指定配置文件
        ''')

def userprofile_bind_group(argv):
    if "-f" in argv:
        file = argv[argv.index("-f")+1]
        filename="%s/%s/%s"%(Base,"conf",file)
        f = open(filename,"r")
        info = yaml.load(f)
        for key,val in info.items():
            print(key)
            print(val)
            from modules.data_init import Userprofiles,Groups
            userprofile_2_group = session.query(Userprofiles).filter(Userprofiles.user==key).first()
            group = session.query(Groups).filter(Groups.groupname==val).first()
            userprofile_2_group.group = [group]
            # session.add(g1)
            session.commit()
    else:
        print('''
        -f 指定配置文件
        ''')

def createhostuser(argv):
    if "-f" in argv:
        file = argv[argv.index("-f")+1]
        filename="%s/%s/%s"%(Base,"conf",file)
        f = open(filename,"r")
        info = yaml.load(f)
        for key,val in info.items():
            from modules.data_init import Hostusers
            u1 = Hostusers(user=key,passwd=info[key]['password'])
            session.add(u1)
            session.commit()
    else:
        print('''
        -f 指定配置文件
        ''')

def userprofile_bind_user(argv):
    if "-f" in argv:
        file = argv[argv.index("-f")+1]
        filename="%s/%s/%s"%(Base,"conf",file)
        f = open(filename,"r")
        info = yaml.load(f)
        for key,val in info.items():
            print(key)
            print(val)
            from modules.data_init import Userprofiles,Hostusers
            userprofile_2_user = session.query(Userprofiles).filter(Userprofiles.user==key).first()
            for i in val:
                user = session.query(Hostusers).filter(Hostusers.user==i).first()
                print(user)
                userprofile_2_user.hostuser = [user]
                # session.add(g1)
                session.commit()
    else:
        print('''
        -f 指定配置文件
        ''')

def Hostusers_bind_group(argv):
    pass
