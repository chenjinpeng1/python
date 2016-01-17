#python 3.5环境,解释器在linux需要改变
#商城购物，阅读手册查询readme文件
#作者：S12-陈金彭


#-------------------------------set集合案例-------------------------------#
#set add()
#语法set.add(self, *args, **kwargs)
'''
Ll=[]   #创建一个列表
S1=set(Ll) #将列表加入集合,
S1.add('chen')
print(S1,Ll)  #>>> {'chen'} [] (列表本身元素并不增加，赋值的集合变量增加)
# 可以直接创建一个集合
S2=set()
S2.add('CHEN')
print(type(S2))  #>>><class 'set'>
#可以将列表设置为集合，但是集合只能add一个元素，不能add多个元素
S1=[1,2,3,4]
S2=set()
S2.add(S1)
print(S2,S1) #>>>TypeError: unhashable type: 'list'
'''
#集合比较
S1=set([1,2,3,4])
S2=set([2,3,5])
print(S1.difference(S2))