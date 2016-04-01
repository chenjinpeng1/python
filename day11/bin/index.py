import sys,os
Base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Base)
from modules import initdata

actions = {
    "initdb":initdata.initdb,
    "create_userprofile":initdata.createuser,
    "create_group":initdata.creategroup,
    "create_host":initdata.createhost,
    "create_hostuser":initdata.createhostuser,
    "userprofile_bind_group":initdata.userprofile_bind_group,
    "userprofile_bind_user":initdata.userprofile_bind_user,
    "hostuser_bind_group":initdata.Hostusers_bind_group
}
def help():
    print('''
    运行程序的初始化操作
    initdb              - init mysql data
    create_userprofile         - create remote user
    create_group        - create group and bind userprofile,
    create_host         - create hosts
    create_hostuser      - create server user
    bind_userprofile    -initdata.userprofile_bind_group
    userprofile_bind_user   - userprofile bind user
    ''')
if __name__=="__main__":
    if len(sys.argv) < 2:
        help()
    else:
        actions[sys.argv[1]](sys.argv[1:])