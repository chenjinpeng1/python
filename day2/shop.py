#----------------------------------------------------------购物车字典--------------------------------------------------------------------------------#
Shopping={
    'Macbook Air':[10,7999],
    'Iphone 6s  ':[10,6543],
    '冰箱       ':[10,3999],
          }
#----------------------------------------------------------用到的变量--------------------------------------------------------------------------------#
Shopping_cart_goods=[] #购物车物品
Shopping_cart_money=0    #购物车金额
Wallet=5000             #账户金额
Shopping_cart=[]           #购物车件数
a = ''
#----------------------------------------------------获取购物车的编号，取值打印显示-----------------------------------------------------------------#
aa=list(Shopping.keys())
for k,val in enumerate(aa):
   a+=''.join([''.rjust(20,' '),str(k),''.center(28,' '),str(val),''.rjust(25,' '),str(Shopping[val][1]),''.center(30,' '),str(Shopping[val][0]),'\n'])
#----------------------------------------------------------进入循环，美化打印----------------------------------------------------------------------------------#
while True:
    Break=False
    print('欢迎来到我的购物中心'.center(100,'❀'))
    print(''.ljust(1,'❀'),''.rjust(165,' '),''.rjust(1,'❀'))
    print('账户名称：陈金彭'.rjust(25,' '),'账户余额：%d'.center(90,' ')%(Wallet),'购物车:%d'.ljust(30,' ')%(len(Shopping_cart_goods)))
    print(''.ljust(1,'❀'),''.rjust(165,' '),''.rjust(1,'❀'))
    print(''.center(102,'❀'),'\n')
    print('商品列表'.center(163,' '))
    print(''.center(170,'='))
    print('编号'.rjust(20,' '),'物品'.rjust(30,' '),'单价'.rjust(30,' '),'余量'.rjust(30,' '))
    print(''.center(170,'='),'\n')
    print(a)
    print(''.center(170,'='))
#----------------------------------------------------------用户输入判断----------------------------------------------------------------------------------#
    Select=input('请输入购买商品的编号：(Q退出)').strip()
    if Select == 'Q':
        LoginSuccess=False
        print('谢谢光临，再见')
        break
    if Select.isdigit() is not True: ##不是Q，不是数字 提示指令错误
            print ('\033[1;31;40m请输入正确的指令\033[0m')
            continue
    if Select.isdigit() is True and int(Select) >= len(Shopping.keys()):
        print ('\033[1;31;40m请输入正确的序列号\033[0m')
        continue
#----------------------------------------------------------购物车物品/金额判断----------------------------------------------------------------------------#
    else:
        Shopping_cart_goods.append(aa[int(Select)])                 #购物车物品变动
        Shopping_cart_money+=Shopping[aa[int(Select)]][1]           #购物车金额变动
        print('商品已加入购物车：')
#----------------------------------------------------------购物车物品结算判定----------------------------------------------------------------------------------#
        while True:
            if Break == True:
                break
            Go_on=input('是否进入购物车结算，Y/N：')
            if Go_on == 'N':
                break
            if Go_on == 'Y':
                while True:
                    for i in Shopping_cart_goods:
                        print ('商品：',str(i),'价格：',Shopping[i][1])
                    print('总金额:%d'%(Shopping_cart_money))
                    Go_on_2=input('是否确认结算，Y/N:')
                    if Go_on_2 == 'N':
                        Break=True
                        break
                    if Go_on_2 == 'Y':
                        if Wallet-Shopping_cart_money >=0:
                            Shopping_cart_goods.clear()
                            Wallet-=Shopping_cart_money
                            print('购买成功,你花费了%d元，剩余%d元'%(Shopping_cart_money,Wallet))
                            Shopping_cart_money=0
                            Break=True
                            break
#----------------------------------------------------------金额超出判断------------------------------------------------------------------------------#
                        else:
                            print('金额不足，请充值或删除购物车的商品继续结算：')
                            Go_on_3=input('删除购物车商品：D 充值：C，退出：Q')
                            if Go_on_3 == 'Q':
                                Break=True
                                break
#----------------------------------------------------------充值----------------------------------------------------------------------------------#
                            elif Go_on_3 == 'C':
                                while True:
                                    print(Wallet)
                                    C_money=input('充值金额：').strip()
                                    if C_money.isdigit()is not True:
                                        print('\033[1;31;40m请输入正确的金额\033[0m')
                                        continue
                                    else:
                                        Wallet+=int(C_money)
                                        print('账户余额：%d'%(Wallet))
                                        Break=True
                                        break
#----------------------------------------------------------购物车物品删除判断----------------------------------------------------------------------------------#
                            elif Go_on_3 == 'D':
                                while True:
                                    for i,val in enumerate(Shopping_cart_goods):
                                        print(i,'商品：',val,'价格：',Shopping[val][1])
                                    Go_on_4=input('请选择删除的商品序号：').strip()
                                    if Go_on_4.isdigit()is not True:
                                        print ('\033[1;31;40m请输入正确的指令\033[0m')
                                        continue
                                    if int(Go_on_4) >= len(Shopping_cart_goods):
                                        print ('\033[1;31;40m请输入正确的序列号\033[0m')
                                        continue
                                    else:
                                        Shopping_cart_money=Shopping_cart_money-Shopping[Shopping_cart_goods[int(Go_on_4)]][1]  #删除物品首先先删除相对应的金额，其次在删除物品栏的物品
                                        Shopping_cart_goods.remove(Shopping_cart_goods[int(Go_on_4)])
                                        Break=True
                                        break
                            else:
                                 print ('\033[1;31;40m请输入正确的指令\033[0m')
                    elif Go_on_2 == 'N':
                        Break=True
                        break
                    else:
                       print ('\033[1;31;40m请输入正确的指令\033[0m')
            else:
                print ('\033[1;31;40m请输入正确的指令\033[0m')
                continue
#----------------------------------------------------------程序完成----------------------------------------------------------------------------------#