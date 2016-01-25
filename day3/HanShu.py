#python 3.5环境，解释器在linux需要改变
#商城购物，阅读手册查询readme文件
#作者：S12-陈金彭
import ha
def Search(arg):
    if arg.isdigit() is True:
        A=ha.Order[ha.AA[int(arg)-1]]
        for i in A:
            print(i)
    else:
        A=ha.Order[arg]
        for i in A:
            print(i.strip('\n'))
def Str_matching(arg):
    try:
        Zh_Input_Dict=ha.json.loads(arg)
        Order_Zh_Input=ha.collections.OrderedDict()
        Order_Zh_Input['server']=Zh_Input_Dict['record']['server']
        Order_Zh_Input['weight']=Zh_Input_Dict['record']['weight']
        Order_Zh_Input['maxconn']=Zh_Input_Dict['record']['maxconn']
        Zh_list=[]
        Zh_Str=' '*8
        Variables=[Zh_Input_Dict,Order_Zh_Input,Zh_list,Zh_Str]
        return Variables
    except Exception:
        Return=False
        return Return
        print('输入格式错误！')
def Write(arg):
    with open('ha.txt','w')as Q:
        for i,val in arg.items():
            i=i+'\n'
            Q.write(i)
            for i in range(len(val)):
                    Q.write(val[i])
                    # print(val[i])
def Zt_PD(arg):
            Del_Input=''.join(['backend ',arg])
            if Del_Input in list(ha.Order.keys()):
                Return=True
            else:
                Return=False
                print('主体不存在！')
            Var=[Del_Input,Return]
            return Var