#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import sys,os,pickle
DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR)
from Card import R_W_config
def Card_main(User):
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
                YueEdu=0
                if info[User][7] > info[User][6]:
                    YueEdu=info[User][7] - info[User][6]
                余额=info[User][7] - int(quxian)
                取现额度=info[User][8]-int(quxian)+YueEdu
                欠款=info[User][9]-int(quxian)+YueEdu
                info[User][7] = 余额
                info[User][8] = 取现额度
                info[User][9] = 欠款
                print(info)
                print('余额 %s，取现额度 %s'%(str(余额),str(取现额度)))
                R_W_config.Write(info)
        if Options == '3':
            print('欠款 %s'%info[User][9])
            huankuan=input('请输入还款的金额：')
            if info[User][9] < 0:
            #     info[User][9] = info[User][9] + int(huankuan)
            #     if info[User][8] + int(huankuan) /2 == 5000:
            #         info[User][8] += int(huankuan) / 2
            #     elif info[User][8] + int(huankuan) /2 > 5000:
            #         info[User][8] + int(huankuan)
            # if info[User][9]  > 0:
                info[User][7] += info[User][9]
                print(info[User][7])
                info[User][9] -= info[User][9]
                print(info[User][9])
            else:
                info[User][7] += int(huankuan)
            R_W_config.Write(info)
            print('还款成功')
        if Options == '4':
            pass
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
