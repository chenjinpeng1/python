#python 3.5环境，解释器在linux需要改变
#商城购物，阅读手册查询readme文件
#作者：S12-陈金彭
B=[]
A={"record":{"server": "100.1.7.999","weight": 20,"maxconn": 30}}
# for i,k in A['record'].items():
#     B.append(i)
#     B.append(k)
# print(B)
B.append(A['record']['server'])
print(B)