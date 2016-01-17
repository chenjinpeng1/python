List=[['MacBook Air',7999],['Starbucks Coffee',33],['Iphone 6Plus',6188]]
a = ''
LoginSuccess=True
for i,val in enumerate(List):
    a+= str(i) + '.   ' + val[0] + '\t'+ str(val[1])+'\n'
while LoginSuccess:
    Money=input('欢迎来到我的商店，请输入你的购物预算：').strip()
    while LoginSuccess:
        print ('''
%s
        '''%a)
        Goods=input('请输入你要购买商品的序列号(退出请按quit)：').strip()
        if Goods == 'quit':
            LoginSuccess=False
            break
        if Goods.isdigit() is not True: ##不是quit，不是数字 提示指令错误
                print ('请输入正确的指令')
                continue
        if Goods.isdigit() is True and int(Goods) >= len(List):
            print ('请输入正确的序列号')
            continue
        if (int(Money)-List[int(Goods)][1]) >= 0:
            print ('购买成功，你花费了%d元，还剩余%d元'%(int(List[int(Goods)][1]),int(int(Money)-List[int(Goods)][1])))
            Money=int(Money)-List[int(Goods)][1]
        else:
            print ('你好，你的购物预算低于购买价格，无法购买！再见')
            LoginSuccess=False
            break
    if LoginSuccess==False:
        print ('谢谢光临，再见')
        break