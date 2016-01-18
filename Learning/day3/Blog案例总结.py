#python 3.5环境,解释器在linux需要改变
#商城购物，阅读手册查询readme文件
#作者：S12-陈金彭


#-------------------------------set集合案例-------------------------------#
#set add()
#语法set.add(self, *args, **kwargs)

# Ll=[]   #创建一个列表
# S1=set(Ll) #将列表加入集合,
# S1.add('chen')
# print(S1,Ll)  #>>> {'chen'} [] (列表本身元素并不增加，赋值的集合变量增加)
# # 可以直接创建一个集合
# S2=set()
# S2.add('CHEN')
# print(type(S2))  #>>><class 'set'>
# #可以将列表设置为集合，但是集合只能add一个元素，不能add多个元素
# S1=[1,2,3,4]
# S2=set()
# S2.add(S1)
# print(S2,S1) #>>>TypeError: unhashable type: 'list'

# set.clear() #清除集合

#set.copy() #浅拷贝一个集合

#差集
#set.difference()
# S1=set([1,2,3,4])
# S2=set([2,3,5])
# print(S1.difference(S2)) #取两个集合之间的差集 {1,4}

#取差集并且更新
#set.difference_update()
# S1=set([1,2,3,4])
# S2=set([2,3,5])
# S1.difference_update(S2)
# print(S1) #>>> {1,4}

# set.discard() #从集合中删除一个元素
# S1=set([1,2,3,4])
# S1.discard(2)
# print(S1) #>>>{1,3,4}

#交集
# set.intersection()
# S1=set([1,2,3,4])
# S2=([2,3,5] )
# S3=S1.intersection(S2)
# print(S3) #>>> {2,3}

#set.intersection_update() #取交集并更新
# S1=set([1,2,3,4])
# S2=set([2,3,5])
# S1.intersection_update(S2)
# print(S1)  # >>> {2,3}

#set.isdisjoint() 判断有没有交集，有返回True，否则返回False
# S1=set([1,2,3,4])
# S2=set([7,6,5])
# print(S1.isdisjoint(S2))  #>>>True

#子集   判断集合中的所有元素是否都是另一个集合的子集，是返回True,
# set.issubset()
# S1=set([1,2,3,4])
# S2=set([2,3])
# print(S2.issubset(S1)) >>> True

#set.issuperset()  判断集合中的所有元素是否是另一个集合的父集，是返回True
# S1=set([1,2,3,4])
# S2=set([2,3])
# print(S1.issuperset(S2)) #>>> True

#set.pop() 删除集合中的第一个元素
# S1=set([1,2,3,4])
# S1.pop()
# print(S1) #{2, 3, 4}

# set.remove() 指定删除集合中的任意一个元素
# S1=set([1,2,3,4])
# S1.remove(2)
# print(S1) #>>> {1, 3, 4}

# set.symmetric_difference() 取交差交集
# S1=set([1,2,3,4])
# S2=set([2,3,5])
# print(S1.symmetric_difference(S2)) #{1, 4, 5}

# set.symmetric_difference_update() 取交差交集
# S1=set([1,2,3,4])
# S2=set([2,3,5])
# S1.symmetric_difference_update(S2)
# print(S1)#>>>{1, 4, 5}

# S1.union()#返回一个新的集合
# S1=set([1,2,3,4])
# S2=set([7,8])
# S3=S1.union(S2)
# print(S3)  #{1, 2, 3, 4, 7, 8}

