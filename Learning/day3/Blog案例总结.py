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

# S1.union()#集合相加，返回一个新的集合
# S1=set([1,2,3,4])
# S2=set([7,8])
# S3=S1.union(S2)
# print(S3)  #{1, 2, 3, 4, 7, 8}



#-------------------------------------collection------------------------------------------#
import collections
#-------------------------------------Counter计数器-----------------------------------------#
#Counter计数器 统计元素中出现元素的次数
# C=('aaaaaaaaaaabbbbbbcccccccccc')
# print(collections.Counter(C)) #Counter({'a': 11, 'c': 10, 'b': 6})
#clear 清除计数器信息
# A=collections.Counter('saascbdmnzuisdd')
# A.clear()
# print(A)
#生成一个字典
# A=collections.Counter(a=4, b=2)
# print(A) #>>>Counter({'a': 4, 'b': 2})
#对于不存在的元素 返回0
# B=A.__missing__('c')
# print(B)
#返回前N个计数器内元素的信息
# A=collections.Counter('aaaabbbccdeeeeeee').most_common(2)
# print(A)
# A=collections.Counter('aaabbc')
# print(sorted(A.elements())) #>>>['a', 'a', 'a', 'b', 'b', 'c'] #sorted等同于以下解释
# B=A.elements()
# for i in B:print(i)

#update() 更新一个计数器,没有则增加，有加1
# A=collections.Counter('aaabbc')
# A.update('e')
# print(A)

#subtract()根据指定的元素的数量删除计数器原来的元素数量
# A=collections.Counter('aaabbc')
# A.subtract('aaae')
# print(A)

# -------------------------------------OrderedDict有序字典------------------------------------------#
# import collections
# # a = collections.OrderedDict()
# # a[1]='a'
# # a[2]='b'
# # print(a) #>>> OrderedDict([(1, 'a'), (2, 'b')])
#
# A=collections.OrderedDict(name='chen',age='25',job='it')
# print(A)
# print(A.keys())
# print(A.values)
# A.update(name='chenjinpeng')
# A.update(time=2016)
# print(A)

# -------------------------------------defaultDict有序字典------------------------------------------#

# A=collections.defaultdict(list)
# A[1]=11
# A[2]=22
# A[3]=33
# print(A)
# print(A.keys())
# print(A.values())
# #有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
# #即： {'k1': 大于66 , 'k2': 小于66}
# Num=[11,22,33,44,55,66,77,88,99]
# A=collections.defaultdict(list)
# for i in Num:
#     if i >= 66:
#         A['k1'].append(i)
#     else:
#         A['k2'].append(i)
# print(A)
# #>>> defaultdict(<class 'list'>, {'k2': [11, 22, 33, 44, 55], 'k1': [66, 77, 88, 99]})

# -------------------------------------defaultdDict有序字典------------------------------------------#

# -------------------------------------可命名元组------------------------------------------#
# Mytuple = collections.namedtuple('Mytuple',['x', 'y', 'z'])
# A=Mytuple(x=1,y=2,z=3)
# print(A.x,A.y,A.z) #>>> 1 2 3
# print(A) # >>> Mytuple(x=1, y=2, z=3)
# print(A[0],A[1],A[2]) #>>> 1 2 3

# -------------------------------------deque双向队列------------------------------------------#

# A=collections.deque([1,2,3,4])
# print(A) # >>> deque([1, 2, 3, 4])
# A.append(5) # 增加一个元组到右侧
# print(A)
# A.appendleft(0) # 增加一个元素到左侧
# print(A)
# A.extend([6,7,8]) #右侧扩展一个列表
# print(A)
# A.extendleft([-1,-2]) # 左侧扩展一个列表
# print(A)
# B=A.count(1) # 匹配队列中元素出现的次数
# print(B)
# A.pop()
# print(A) # 删除队列中的最后一个元素
# A.popleft()
# print(A) # 删除队列中第一个元素 从左边开始
# A.remove(2)
# print(A) # 删除队里中指定的元素
# A.reverse()
# print(A) #反转队列
# A.rotate()
# print(A) #将队列中最后N个元素移动至最前
# '''
# deque([1, 2, 3, 4])
# deque([1, 2, 3, 4, 5])
# deque([0, 1, 2, 3, 4, 5])
# deque([0, 1, 2, 3, 4, 5, 6, 7, 8])
# deque([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
# 1
# deque([-2, -1, 0, 1, 2, 3, 4, 5, 6, 7])
# deque([-1, 0, 1, 2, 3, 4, 5, 6, 7])
# deque([-1, 0, 1, 3, 4, 5, 6, 7])
# deque([7, 6, 5, 4, 3, 1, 0, -1])
# deque([-1, 7, 6, 5, 4, 3, 1, 0])
# '''

# -------------------------------------单向队列------------------------------------------#
#
# import queue
# B=queue.Queue()
# print(B.empty())
# B.put('aaaa')
# B.put('bbbb')
# print(B.qsize())
# print(B.get())
# print(B.get_nowait())



#迭代器
