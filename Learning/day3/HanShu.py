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
# def Write(**arg):
#     with open('test.log','w')as Q:
#         for i,val in arg.items():
#             i=i+'\n'
#             print(i)
#             if isinstance(val,dict) is True:
#                 print(val)
#             else:
#                 for i in range(len(val)):
#                     print(val[i])
