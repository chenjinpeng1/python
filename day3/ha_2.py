# #python 3.5环境，解释器在linux需要改变
# #商城购物，阅读手册查询readme文件
# #作者：S12-陈金彭
# import HanShu
# import collections
# import json
# Options=['增加','删除','修改','查询']
# Order=collections.OrderedDict()
# with open('ha.txt') as obj:
#     for i in obj.readlines():
#         if len(i[:3].strip()) > 0:
#             B=i.strip()
#             Order[B] = []
#         else:
#             Order[B].append(i)
# AA=list(Order.keys())
# if __name__=="__main__":
#     for i,val in enumerate(Options,1):
#         print(i,val)
#     Input=input('请输入你要执行的操作：')
#     if int(Input) == 1:
#         print ('''
#         1.增加主体
#         2.增加主体信息
#         ''')
#         Input=input('请选择要增加的类型：')
#         while True:
#             if int(Input) == 1:
#                 Exit=True
#                 Add_Input=input('主体信息：')
#                 Variables=HanShu.Str_matching(Add_Input)
#                 for ii,val in Variables[0].items():
#                     if ii == 'backend':
#                         Str=' '.join([ii,val])
#                 for i in Order.keys():
#                     if Str in i:
#                         print('主体已经存在！！！')
#                         Exit=False
#                 if Exit:
#                     for ii,v in Variables[1].items():
#                         Variables[2].extend([''.join([ii,' ',str(v)])])
#                     for ii in range(len(Variables[2])):
#                         Variables[3]+=' '.join([Variables[2][ii],' '])
#                     Variables[3]+='\n'
#                     Order[Str]=[Variables[3]]
#                     HanShu.Write(Order)
#             if int(Input) == 2:
#                 ZT_name=input('主体名称：').strip()
#                 ZT_name=''.join(['backend ',ZT_name])
#                 if ZT_name in list(Order.keys()):
#                     Return=True
#                 else:
#                     Return=False
#                     print('主体不存在！')
#                     break
#                 if Return:
#                     Add_Input=input('主体信息：')
#                     Variables=HanShu.Str_matching(Add_Input)
#                     for i,val in Variables[1].items():
#                         Variables[2].append(''.join([i,' ',str(val)]))
#                     for i in Variables[2]:
#                         Variables[3]+=''.join([i,' '])
#                     Variables[3]+='\n'
#                     Order[ZT_name].extend([Variables[3]])
#                     HanShu.Write(Order)
#     if int(Input) == 2:
#         print('''
#         1.删除主体
#         2.删除主体信息
#         ''')
#         Input=input('选择删除的类型：')
#         if int(Input) == 1:
#             Del_Input=input('删除主体名称：')
#             Del_Input=''.join(['backend ',Del_Input])
#             print(Del_Input)
#             if Del_Input in list(Order.keys()):
#                 Order.pop(Del_Input)
#                 # print(Order)
#                 HanShu.Write(Order)
#         if int(Input) == 2:
#             Del_Input=input('输入主体名称：')
#             Del_Input=''.join(['backend ',Del_Input])
#             if Del_Input in list(Order.keys()):
#                 Return=True
#             else:
#                 Return=False
#                 print('主体不存在！')
#             if Return:
#                 Del_Value=input('删除的信息：')
#                 Variables=HanShu.Str_matching(Del_Value)
#                 for ii,v in Variables[1].items():
#                     Variables[2].extend([''.join([ii,' ',str(v)])])
#                 for ii in range(len(Variables[2])):
#                     Variables[3]+=' '.join([Variables[2][ii],' '])
#                 Variables[3]+='\n'
#                 Order[Del_Input].remove(Variables[3])
#                 HanShu.Write(Order)
#     if int(Input) == 4:
#         for n,val in enumerate(AA,1):
#             print(n,val)
#         Input=input('输入查询的内容或者序列号：')
#         HanShu.Search(Input)            # 调用查询操作函数
a=['a',1,'b']
aa=a.index('b')
print(aa)
