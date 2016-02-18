#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import sys,os,random,pickle,time
DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR)
print(DIR)
from Card import R_W_config,login
def zhuce():
    Card=''
    while True:
        # Info={}
        Info=R_W_config.Read()
        # Info.pop('root')
        # Info.pop('陈金彭')
        User=input('请输入你的姓名：')
        ID=input('输入你的身份证号码（18位）：')
        City=input('所在城市：')
        Phone=input('输入手机号码：')
        Passwd=input('输入网银密码:')
        信用额度=input('信用额度：')
        取现额度=int(信用额度) /2
        余额=信用额度
        A='10'
        Curent_m=time.strftime("%Y-%m",time.gmtime())
        Curent_m=Curent_m.replace(time.strftime("%m",time.gmtime()),str(int(time.strftime("%m",time.gmtime()))+1))
        Bill_time=('%s-%s'%(Curent_m,A))
        欠款=[0,Bill_time,0,0]
        管理员账户=input('是否为管理员账户（1.是 | 0.不是）：')
        for i in range(0,16):
            Card_random=random.randint(0,9)
            Card += str(Card_random)
        Info[User]=[User,ID,City,Phone,str(Card),Passwd,int(信用额度),int(余额),取现额度,欠款,管理员账户]
        R_W_config.Write(Info)
        State='注册-%s'%User
        W_log=R_W_config.Read_log()
        W_log[User].append('%s       %s      %s'%(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),User,State))
        R_W_config.Write_log(W_log)
        print('你好 %s 你的卡号为%s 信用额度为%s'%(User,Card,信用额度))
        login.login(User,Passwd)


