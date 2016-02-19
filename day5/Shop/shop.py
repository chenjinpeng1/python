#python 3.5环境，解释器在linux需要改变
#商城购物，阅读手册查询readme文件
#调用文件 login.txt,lock.txt
#作者：S12-陈金彭
import os,sys,time
DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR)
from Shop import Shop_HS
def shop():
    Auth_File="Shop/login.txt"                               #认证登陆文件
    Lock_File="Shop/lock.txt"                                #锁定文件
    F_Auth = open(Auth_File)
    Read_Auth=F_Auth.readlines()                          #执行前将账号密码文件读取到变量，避免循环读取
    F_Auth.close()
    User_Exit=[]
    while True:
        LoginSusses=False                               #循环开始前先定义登陆成功失败的变量。方便循环嵌套跳转
        Auth=True
        count = 0                                        #定义计数器，错误三次锁定
        Read_Lock=open(Lock_File)                        #读取锁文件到变量Lock_List
        Lock_List=[]
        for i in Read_Lock.readlines():
            line = i.strip('\n')
            a = Lock_List.append(line)
        Read_Lock.close()
        ZL_List=['注册','登陆']
        for index,i in enumerate(ZL_List,1):print(index,i)
        ZL=input('选择操作')
        if ZL == '1':
            Name=input('注册用户名：')
            Pass=input('输入密码')
            Dir_File=open('Shop/login.txt',"a")
            Dir_File.write('%s %s %d %s'%(Name,Pass,5000,'\n'))
            Dir_File.close()
            LoginSusses=True
            break
        elif ZL == '2':
            Name=input('请输入你的账户:').strip()
            for i in Read_Auth:
                i = i.split()
                if len(i) != 0:
                    User_Exit.append(i[0])
            if Name not in User_Exit:
                print('你输入的用户名不存在！')
                # Auth=False
                break
            if Name in Lock_List:
                print("你的账户已经被锁定！！请联系管理员解锁！")             #，用户登陆前先判断用户是否被锁定后在进行密码判断。
                Auth=False
                break
            for line in Read_Auth:
                line = line.split()
                if Name in line:
                    for i in range(3):                              #定义3次循环，
                        Passwd=input('请输入你的密码：')
                        if Passwd == line[1]:
                            LoginSusses=True
                            break
                        else:
                            print ("你的密码错误，请重新输入")
                            count +=1                                       #每次密码错误后计数器count+1,3次后锁定，写入锁文件
                        if count == 3:
                            f = open(Lock_File,'a')
                            f.write('%s\n'%Name)
                            f.close()
                            print ("你的密码错误次数达到3次，已被锁定")
                            Auth=False
                    if LoginSusses is True:break                                #跳出2层循环
                if count ==3:                                                     #锁定用户后跳出2层循环
                    break
            if LoginSusses is True:                                             #跳出2层循环
                break
        if Auth==False:break
    if LoginSusses==True:
        print("Good，欢迎您登陆：%s" %Name)

        #----------------------------------------------------------购物车字典--------------------------------------------------------------------------------#
        Shopping={
            'Macbook Air':[10,7999],
            'Iphone 6s  ':[10,6543],
            '冰箱       ':[10,3999],
                  }
        #----------------------------------------------------------用到的变量--------------------------------------------------------------------------------#
        Shopping_cart_goods=[] #购物车物品
        Shopping_cart_money=0    #购物车金额
        for i in open(Auth_File,'r'):  #  #账户金额
            i=i.split()
            if i[0] == Name:
                Wallet=int(i[2])
        Num=10           #购物车件数
        #--------------------------------------------------------------------进入循环------------------------------------------------------------------------#
        while True:
            LoginSusses=True
            LoginSusses2=True
        #----------------------------------------------------获取购物车的编号，取值打印显示------------------------------------------------------------------#
            a = ''
            aa=list(Shopping.keys())
            for k,val in enumerate(aa):
               a+=''.join([''.rjust(20,' '),str(k),''.center(28,' '),str(val),''.rjust(25,' '),str(Shopping[val][1]),''.center(30,' '),str(Shopping[val][0]),'\n'])
         #-------------------------------------------------------------进入循环，美化打印--------------------------------------------------------------------#
            print('欢迎来到我的购物中心'.center(100,'❀'))
            print(''.ljust(1,'❀'),''.rjust(165,' '),''.rjust(1,'❀'))
            print('账户名称：%s'.rjust(25,' ')%(Name),'账户余额：%d'.center(90,' ')%(Wallet),'购物车:%d'.ljust(30,' ')%(len(Shopping_cart_goods)))
            print(''.ljust(1,'❀'),''.rjust(165,' '),''.rjust(1,'❀'))
            print(''.center(102,'❀'),'\n')
            print('商品列表'.center(163,' '))
            print(''.center(170,'='))
            print('编号'.rjust(20,' '),'物品'.rjust(30,' '),'单价'.rjust(30,' '),'余量'.rjust(30,' '))
            print(''.center(170,'='),'\n')
            print(a)
            print(''.center(170,'='))
        #----------------------------------------------------------用户输入判断-------------------------------------------------------------------------------#
            Select=input('请输入购买商品的编号：(Q退出)').strip()
            if Select == 'Q':
                print('谢谢光临，再见')
                break
            if Select.isdigit() is not True: ##不是Q，不是数字 提示指令错误
                    print ('\033[1;31;40m请输入正确的指令\033[0m')
                    continue
            if Select.isdigit() is True and int(Select) >= len(Shopping.keys()):
                print ('\033[1;31;40m请输入正确的序列号\033[0m')
                continue
        #----------------------------------------------------------购物车物品/金额判断------------------------------------------------------------------------#
            else:
                Shopping_cart_goods.append(aa[int(Select)])                 #购物车物品变动
                Shopping_cart_money+=Shopping[aa[int(Select)]][1]           #购物车金额变动
                Shopping[aa[int(Select)]][0]-=1
                print('商品已加入购物车：')
        #----------------------------------------------------------购物车物品结算判定-------------------------------------------------------------------------#
                while True:
                    if LoginSusses==False:
                        break
                    Go_on=input('是否进入购物车结算，Y/(任意键继续)：')
                    if Go_on != 'Y':
                        break
                    if Go_on == 'Y':
                        while True:
                            for i in Shopping_cart_goods:
                                print ('商品：',str(i),'价格：',Shopping[i][1])
                            print('总金额:%d'%(Shopping_cart_money))
                            if Wallet-Shopping_cart_money >=0:
                                Shopping_cart_goods.clear()
                                Wallet-=Shopping_cart_money
                                print('购买成功,你花费了%d元，剩余%d元'%(Shopping_cart_money,Wallet))
                                Shopping_cart_money=0
     #----------------------------------------------------------金额写入文件------------------------------------------------------------------------------#
                                b=''
                                with open('login.txt','r') as f:
                                    for i in f.readlines():
                                        a=i.split()
                                        if 'chenjinpeng' in i:
                                            i=i.replace(str(a[2]),str(Wallet))
                                        b+=i
                                with open('login.txt','w') as f:
                                    f.write(b)
                                LoginSusses=False
                                break
        #----------------------------------------------------------金额超出判断------------------------------------------------------------------------------#
                            else:
                                print('金额不足，按提示操作：')
                                Go_on_1=input('删除购物车商品：D 信用卡付款：C，退出：Q')
                                if Go_on_1 == 'Q':
                                    LoginSusses2=False
                                    LoginSusses=False
        #----------------------------------------------------------退出时，金额写入文件------------------------------------------------------------------------------#
                                    b=''
                                    with open(Auth_File,'r') as f:
                                        for i in f.readlines():
                                            a=i.split()
                                            if 'chenjinpeng' in i:
                                                i=i.replace(str(a[2]),str(Wallet))
                                            b+=i
                                    with open(Auth_File,'w') as f:
                                        f.write(b)
                                        break
        #----------------------------------------------------------信用卡结算----------------------------------------------------------------------------------#
                                elif Go_on_1 == 'C':
                                    Fk_result=Shop_HS.Card_fk(Shopping_cart_money)
                                    if Fk_result != False:
                                        if Fk_result != 2:
                                            if Fk_result:
                                                Shopping_cart_goods.clear()
                                                LoginSusses=False
                                                break
                                            else:
                                                print('等有钱了在来买吧...')
                                                break

        #----------------------------------------------------------购物车物品删除判断----------------------------------------------------------------------------------#
                                elif Go_on_1 == 'D':
                                    while True:
                                        for i,val in enumerate(Shopping_cart_goods):
                                            print(i,'商品：',val,'价格：',Shopping[val][1])
                                        Go_on_2=input('请选择删除的商品序号：').strip()
                                        if Go_on_2.isdigit()is not True:
                                            print ('\033[1;31;40m请输入正确的指令\033[0m')
                                            continue
                                        if int(Go_on_2) >= len(Shopping_cart_goods):
                                            print ('\033[1;31;40m请输入正确的序列号\033[0m')
                                            continue
                                        else:
                                            Shopping_cart_money=Shopping_cart_money-Shopping[Shopping_cart_goods[int(Go_on_2)]][1]  #删除物品首先先删除相对应的金额，其次在删除物品栏的物品
                                            Shopping_cart_goods.remove(Shopping_cart_goods[int(Go_on_2)])
                                            Shopping[aa[int(Select)]][0]+=1
                                            break
                                else:
                                     print ('\033[1;31;40m请输入正确的指令\033[0m')
                    else:
                        print ('\033[1;31;40m请输入正确的指令\033[0m')
                        continue
                if LoginSusses2==False:
                    print('谢谢光临，再见!!!!!')
                    break

        #----------------------------------------------------------程序完成----------------------------------------------------------------------------------#