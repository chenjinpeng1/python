#python 3.5环境，解释器在linux需要改变
#信用卡主菜单，阅读手册查询readme文件
#作者：S12-陈金彭
import os,sys,random
DIR=os.path.dirname(os.path.abspath(__file__))
sys.path.append(DIR)
import zhuce,login,Card_main
def main():
    Login_Function=['注册','登陆',]
    print('欢迎登陆信用卡程序')
    for index,i in enumerate(Login_Function,1):
        print(index,i)
    LZ=input('请选择操作：')
    if LZ == '1':
        print('进入注册接口')
        Panduan=zhuce.zhuce()
    if LZ == '2':
        print('进入登陆接口')
        User=input('输入你的账号：')
        Passwd=input('输入你的密码：')
        f=login.login(User,Passwd)
