#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import sys,os,pickle,time,datetime,collections
DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR)
from Card import R_W_config
def Card_main(User):
    # info=R_W_config.Read()
    # A=info[User][8] # 设定临时变量存储取现额度，以便方便计算取现
    while True:
        Main_Function=['账户信息','取现','还款','消费账单','操作日志','删除账户','Exit']
        for index,i in enumerate(Main_Function,1):print(index,i)
        Options=input('请选择所作操作：')
        if Options == '1':
            lixi(User)
            info=R_W_config.Read()
            print(info)
            print('''信用额度：%s 余额：%s 欠款%s 取现额度%s

            '''%(info[User][6],info[User][7],info[User][9][0],info[User][8]))
        if Options == '2':
            info=R_W_config.Read()
            quxian=input('请输入你要取现的金额：')
            if int(quxian) > info[User][8]:
                print('超出取现额度，取现额度为%s'%str(info[User][8]))
            elif int(quxian) > info[User][7]:
                print('余额不足')
            else:
                YueEduo=0
                if info[User][7] > info[User][6]:
                    YueEduo=info[User][7] - info[User][6]
                余额=info[User][7] - int(quxian)
                取现额度=info[User][8]-int(quxian)
                欠款=int(info[User][9][0]-int(quxian)+YueEduo)
                info[User][7] = 余额
                info[User][8] = 取现额度
                info[User][9][0] = 欠款
                print('余额 %s，取现额度 %s'%(str(余额),str(取现额度)))
                R_W_config.Write(info)
                log=R_W_config.Read_XF()
                # log=collections.defaultdict(list)
                log[User].append('%s  %s     %s          %s'%(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) ,Main_Function[int(Options)-1],quxian))
                R_W_config.Write_XF(log)
        if Options == '3':
            lixi(User)
            info=R_W_config.Read()
            print('欠款 %s'%abs(info[User][9][0]))
            huankuan=input('请输入还款的金额：')
            info[User][9][0]+=float(huankuan)
            if info[User][9][0] >= 0:
                info[User][9][0] = 0
                info[User][9][2] = 0
                info[User][9][3] = 0
                A='10'
                Curent_m=time.strftime("%Y-%m",time.gmtime())
                Curent_m=Curent_m.replace(time.strftime("%m",time.gmtime()),str(int(time.strftime("%m",time.localtime()))+1))
                Bill_time=('%s-%s'%(Curent_m,A))
                info[User][9][1]=Bill_time
            info[User][7]+=float(huankuan )
            info[User][8] = info[User][6] /2 + (info[User][7]-info[User][6])
            R_W_config.Write(info)
            log=R_W_config.Read_XF()
            log[User].append('%s  %s     %s          %s'%(User,time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) ,Main_Function[int(Options)-1],huankuan))
            R_W_config.Write_XF(log)
            print('还款成功')
        if Options == '4':
            log=R_W_config.Read_XF()
            for i in range(len(log[User])):print(log[User][i])
        if Options == '5':
            log=R_W_config.Read_log()
            for i in range(len(log[User])):print(log[User][i])
        if Options == '6':
            info=R_W_config.Read()
            if info[User][10] != '1':
                print('非管理员，不具备删除权限，请联系管理员')
            else:
                Del_user=input('请输入你要删除的账户：')
                if info.get(Del_user) is None:
                    print('该用户不存在')
                else:
                    info.pop(Del_user)
                    R_W_config.Write(info)
                    State='删除-%s'%Del_user
                    # W_log=collections.defaultdict(list)
                    W_log=R_W_config.Read_log()
                    W_log[User].append('%s       %s      %s'%(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),User,State))
                    R_W_config.Write_log(W_log)
                    print('删除成功')
        if Options == '7':
            break
def lixi(User):
    info = R_W_config.Read()
    逾期=info[User][9][1].split('-')
    Curent_m=(time.strftime("%Y-%m-%d",time.gmtime())) #当前时间
    A=Curent_m.split('-')
    逾期年=int(A[0])-int(逾期[0])
    逾期月=int(A[1])-int(逾期[1])
    逾期日=int(A[2])-int(逾期[2])
    info[User][9][3]=(逾期年 * 365)+(逾期月)*30+逾期日
    if abs(info[User][9][0]) !=0: #判断是否欠款
        if info[User][9][3] > 0:  #判断是否逾期
            A=info[User][9][2]
            for i in range(info[User][9][3]):
                A=info[User][9][0] * 0.0005 #计算利息
                info[User][9][1]=Curent_m #重新赋值逾期时间
                info[User][9][0]+=A #欠款
                info[User][9][2]+=A #利息
                info[User][7]+=A #余额（减去利息 由于利息为-值，则为加）
            info[User][9][0]=float('%.3f'%info[User][9][0])
            info[User][9][2]=float('%.3f'%info[User][9][2])
            info[User][7]=float('%.3f'%info[User][7])
            R_W_config.Write(info)
            R_W_config.Read()