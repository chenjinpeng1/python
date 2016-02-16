#python 3.5环境，解释器在linux需要改变
# ，阅读手册查询readme文件
#作者：S12-陈金彭
import os,sys,pickle
from Card import R_W_config,Card_main
DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR)
def login(user,passwd):
    info=R_W_config.Read()
    print(info)
    if user in info.keys() and passwd == info[user][5]:
        print('登陆成功！')
        Card_main.Card_main(user)
    else:print('账号密码错误')