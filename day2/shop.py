# List=[['MacBook Air',7999],['Starbucks Coffee',33],['Iphone 6Plus',6188]]
Shopping={
    'Macbook Air':[10,7999],
    'Iphone 6s  ':[10,6543],
    '冰箱       ':[10,3999],
          }
Success=True
Shopping_cart_goods=[]
Shopping_cart_money=0    #购物车金额
Wallet=50000             #账户金额
Shopping_cart=0           #购物车件数
a = ''
aa=list(Shopping.keys())
for k,val in enumerate(aa):
   a+=''.join([''.rjust(20,' '),str(k),''.center(28,' '),str(val),''.rjust(25,' '),str(Shopping[val][0]),''.center(30,' '),str(Shopping[val][1]),'\n'])
print(a)
while Success:
    print('欢迎来到我的购物中心'.center(100,'❀'))
    print(''.ljust(1,'❀'),''.rjust(165,' '),''.rjust(1,'❀'))
    print(''.ljust(1,'❀'),'账户名称：陈金彭'.rjust(25,' '),'账户余额：%d'.center(90,' ')%(Wallet),'购物车:%d'.ljust(30,' ')%(Shopping_cart),''.ljust(1,'❀'))
    print(''.ljust(1,'❀'),''.rjust(165,' '),''.rjust(1,'❀'))
    print(''.center(102,'❀'),'\n')
    print('商品列表'.center(163,' '))
    print(''.center(170,'='))
    print('编号'.rjust(20,' '),'物品'.rjust(30,' '),'单价'.rjust(30,' '),'余量'.rjust(30,' '))
    print(''.center(170,'='),'\n')
    print(a)
    print(''.center(170,'='))
    Select=input('请输入购买商品的编号：(Q退出)').strip()
    if Select == 'Q':
        LoginSuccess=False
        break
    if Select.isdigit() is not True: ##不是quit，不是数字 提示指令错误
            print ('请输入正确的指令')
            continue
    if Select.isdigit() is True and int(Select) >= len(Shopping.keys()):
        print ('请输入正确的序列号')
        continue
    else:
        Shopping_cart+=1
        Shopping_cart_goods.append(aa[int(Select)])              #购物车物品变动
        Shopping_cart_money+=Shopping[aa[int(Select)]][1]           #购物车金额变动
        # print(Shopping_cart_money)
        # print(Shopping_cart_goods)
        print('商品已加入购物车：')
        Go_on=input('是否进入购物车结算，Y/N：')
        if Go_on == 'Y':
            for i in Shopping_cart_goods:
                print ('商品：',str(i),'价格：',Shopping[i][1])
            print('总金额:%d'%(Shopping_cart_money))
            Go_on_2=input('是否确认结算，Y/N:')
            if Go_on_2 == 'Y':
                Wallet=Wallet-Shopping_cart_money
                if Wallet >=0:
                    print('购买成功,你花费了%d元，剩余%d元'%(Shopping_cart_money,Wallet))
                else:
                    print('金额不足，请充值或删除购物车的商品继续结算：')
                    Go_on_3=input('删除购物车商品：D 充值：C，退出：Q')
                    if Go_on_3 == 'Q':
                        break
                    if Go_on_3 == 'D':
                        for i,val in enumerate(Shopping_cart_goods):
                            print(i,'商品：',val,'价格：',Shopping[val][1])
                        Go_on_4=input('请选择删除的商品序号：').strip()
                        if Go_on_4.isdigit()is not True:
                            print('请输入正确的指令！')
                            continue
                        if Go_on_4 > len(Shopping_cart_goods):
                            print('请输入正确的序列号！')
                            continue

    # if (int(Money)-List[int(Goods)][1]) >= 0:
    #     print ('购买成功，你花费了%d元，还剩余%d元'%(int(List[int(Goods)][1]),int(int(Money)-List[int(Goods)][1])))
    #     Money=int(Money)-List[int(Goods)][1]
    # else:
    #     print ('你好，你的购物预算低于购买价格，无法购买！再见')
    #     LoginSuccess=False
    #     break
    # if LoginSuccess==False:
    # print ('谢谢光临，再见')
    # break