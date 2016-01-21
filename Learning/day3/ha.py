#python 3.5环境，解释器在linux需要改变
#商城购物，阅读手册查询readme文件
#作者：S12-陈金彭
import collections
# A=collections.OrderedDict()
# with open('ha.txt','r') as obj:
#     for i in obj.readlines():
#         if len(i.strip()) <= 0:
#             continue
#         else:
#             i = i.strip().split('\n')
#             A[i]
# with open('ha.txt','a') as obj:

# Input=input('请输入backend：')
# with open('ha.txt','a') as obj:
# import json
# Input = input('请输入要新加的记录：')
# Input=json.loads(Input)
# A=Input['backend']
# B=Input['record']
# D=str(' '*4)+'server'+' '+B['server']+' '+'weight'+' '+str(B['weight'])+' '+'maxconn'+' '+str(B['maxconn'])
# with open('ha.txt','r') as obj:
#     for i in obj.readlines():
#         if len(i.strip()) <=0:
#             continue
#         else:
#             i=i.split('\n')
#             if 'test.oldboy.org' in i:
#                 obj.write(D)

import HanShu
import collections
import json
Options=['增加','删除','修改','查询']
Order=collections.OrderedDict()
with open('ha.txt') as obj:
    for i in obj.readlines():
        if len(i[:3].strip()) > 0:
            B=i.strip()
            Order[B] = []
        else:
            Order[B].append(i)
AA=list(Order.keys())
if __name__=="__main__":
    for i,val in enumerate(Options,1):
        print(i,val)
    Input=input('请输入你要执行的操作：')
    if int(Input) == 1:
        print ('''
        1.增加主体
        2.增加主体信息
        ''')
        Input=input('请选择要增加的类型：')
        if int(Input) == 1:
            Add_Input=input('主体信息：')
            Zh_Input_Dict=json.loads(Add_Input)
            Order_Zh_Input=collections.OrderedDict()
            Order_Zh_Input['server']=Zh_Input_Dict['record']['server']
            Order_Zh_Input['weight']=Zh_Input_Dict['record']['weight']
            Order_Zh_Input['maxconn']=Zh_Input_Dict['record']['maxconn']
            Zh_list=[]
            Zh_Str=' '*8
            for ii,val in Zh_Input_Dict.items():
                if ii == 'backend':
                    Str=' '.join([ii,val])
            for i in Order.keys():
                Exit=True
                if Str in i:
                    print('主体已经存在！！！')
                    break
            for ii,v in Order_Zh_Input.items():
                Zh_list.extend([''.join([ii,' ',str(v)])])
            for ii in range(len(Zh_list)):
                Zh_Str+=' '.join([Zh_list[ii],' '])
            Zh_Str+='\n'
            Order[Str]=[Zh_Str]
            print(Order)
            HanShu.Write(Order)
        if int(Input) == 2:
            while True:
                Add_Input=input('主体名称：').strip()
                for ii in list(Order.keys()):
                    if Add_Input in ii:
                        ZT_Information=input('主体信息：')
                        Zh_Input_Dict=json.loads(ZT_Information)
                        Order_Zh_Input=collections.OrderedDict()
                        Order_Zh_Input['server']=Zh_Input_Dict['record']['server']
                        Order_Zh_Input['weight']=Zh_Input_Dict['record']['weight']
                        Order_Zh_Input['maxconn']=Zh_Input_Dict['record']['maxconn']
                        Zh_list=[]
                        Zh_Str=' '*8
                        for i,val in Order_Zh_Input.items():
                            Zh_list.append(''.join([i,' ',str(val)]))
                        for i in Zh_list:
                            Zh_Str+=''.join([i,' '])
                        Zh_Str+='\n'
                        print(Zh_Str)
                        Order[ii].extend([Zh_Str])
                        print(Order)
                        HanShu.Write(Order)
                else:print('主体名称不存在，重新输入：')
                    # for i in Order.keys():
                    #     if Add_Input in i:
                    #         Order[i].append[Zh_Str]
                    # Order[Str]=[Zh_Str]
                    # HanShu.Write(Order)
    if int(Input) == 4:
        for n,val in enumerate(AA,1):
            print(n,val)
        Input=input('输入查询的内容或者序列号：')
        HanShu.Search(Input)            # 调用查询操作函数

