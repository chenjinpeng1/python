#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import sys,os,pickle,time
DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR)
from Card import R_W_config
def Card_main(User):
    info=R_W_config.Read()
    A=info[User][8] # 设定临时变量存储取现额度，以便方便计算取现
    while True:
        info=R_W_config.Read()
        Main_Function=['账户信息','取现','还款','消费账单','操作日志','删除账户','Exit']
        for index,i in enumerate(Main_Function,1):print(index,i)
        Options=input('请选择所作操作：')
        if Options == '1':
            print('''信用额度：%s 余额：%s 欠款%s 取现额度%s

            '''%(info[User][6],info[User][7],info[User][9],info[User][8]))
        if Options == '2':
            quxian=input('请输入你要取现的金额：')
            if int(quxian) > info[User][8]:
                print('超出取现额度，取现额度为%s'%str(info[User][8]))
            else:
                YueEduo=0
                if info[User][7] > info[User][6]:
                    YueEduo=info[User][7] - info[User][6]
                余额=info[User][7] - int(quxian)
                取现额度=info[User][8]-int(quxian)
                欠款=info[User][9]-int(quxian)+YueEduo
                info[User][7] = 余额
                info[User][8] = 取现额度
                info[User][9] = 欠款
                print(info)
                print('余额 %s，取现额度 %s'%(str(余额),str(取现额度)))
                R_W_config.Write(info)
                log=('时间 %s 操作 %s 金额 %s %s'%(time.ctime(),Main_Function[2],quxian,'\n'))
                print(log)
                R_W_config.Write_XF(log)
        if Options == '3':

            print('欠款 %s'%info[User][9])
            huankuan=input('请输入还款的金额：')
            info[User][9]+=int(huankuan)
            if info[User][9] > 0:
                info[User][9] = 0
            info[User][7]+=int(huankuan )
            # info[User][8]=info[User][7]-info[User][6]+A
            info[User][8] = info[User][6] /2 + (info[User][7]-info[User][6])
            R_W_config.Write(info)
            print('还款成功')
        if Options == '4':
            R_W_config.Read_XF()
        if Options == '5':
            pass
        if Options == '6':
            if info[User][10] != str(1):
                print('非管理员，不具备删除权限，请联系管理员')
            else:
                Del_user=input('请输入你要删除的账户：')
                if info.get(Del_user) is None:
                    print('该用户不存在')
                else:
                    info.pop(Del_user)
                    R_W_config.Write(info)
                    print('删除成功')
        if Options == '7':
            break
