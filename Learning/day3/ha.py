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
Order=collections.OrderedDict()
with open('ha.txt') as obj:
    for i in obj.readlines():
        if len(i[:3].strip()) > 0:
            B=i.strip('\n')
            Order[B] = []
        else:
            Order[B].append(i.strip('\n'))
AA=list(Order.keys())
if __name__=="__main__":
    for n,val in enumerate(AA,1):
        print(n,val)
    Input=input('输入查询的内容或者序列号：')
    HanShu.Search(Input)






















# import collections
# A=collections.OrderedDict(name='chen',age='25',job='it')
# print(A)
# # print (A.keys())
# # print(A.keys())
# # print(A.values())
# # A.update(name='chenjinpeng')
# # A.update(time=2016)
# # print(A)
# # print(type(A))
# for k,v in A.items():
#     print (k)