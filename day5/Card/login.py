#python 3.5环境，解释器在linux需要改变
# ，阅读手册查询readme文件
#作者：S12-陈金彭
import os,sys,pickle,time,collections
from Card import R_W_config,Card_main
DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR)
def login(user,passwd):
    info=R_W_config.Read()
    if user in info.keys() and passwd == info[user][5]:
        State='登陆成功'
        print(State)
        # W_log=collections.defaultdict(list)
        W_log=R_W_config.Read_log()
        W_log[user].append('%s       %s      %s'%(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),user,State))
        R_W_config.Write_log(W_log)
        Card_main.Card_main(user)
    else:
        if user in info.keys():
            State='登陆失败'
            print(State,'检查你的账号密码')
            W_log=R_W_config.Read_log()
            W_log[user].append('%s       %s      %s'%(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),user,State))
            R_W_config.Write_log(W_log)
    if user not in info.keys():
        print('登陆失败！')