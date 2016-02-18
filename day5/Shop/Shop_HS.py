#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import os,sys,time
DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# print(BASE_DIR, 'Card/config.txt')
# os.path.join(BASE_DIR,'\/Card/config.txt')
from Card import R_W_config
def Card_fk(Money):
    print('暂只支持广发银行信用卡')
    Band_List=['广发银行信用卡',]
    for index,i in enumerate(Band_List,1):print(index,i)
    Band=input('请选择你的银行：')
    if Band=='1':
        User=input('请输入账号：')
        Passwd=input('请输入密码：')
        info=R_W_config.Read()
        print(info)
        print('调用信用卡付款')
        if User in info.keys() and Passwd == info[User][5]:
            print('验证通过！')
            print('付款金额 %s'%Money)
            if info[User][7]-Money >= 0:
                info[User][7]-=Money
                info[User][9][0]-=Money
                print('付款成功')
                R_W_config.Write(info)
                log='%s  %s     %s          %s  %s'%(User,time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()) ,'银联消费',Money,'\n')
                R_W_config.Write_XF(log)
                return True
            else:
                print('余额不足')
        else:
            print('账号密码错误')
            return False
    else:
        print('请选择正确的操作！')
        return 2
