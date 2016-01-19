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
# A.move_to_end('name') # 将元素（k,val）移动到最后
# print(A)

# -------------------------------------defaultDict默认字典------------------------------------------#

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
# import queue
# B=queue.Queue()
# print(B.empty()) #如果队列为空，返回True,反之False
# print(B.full()) #如果队列满了，返回True,反之False
# B.put('aaaa') #队列里插入数据
# B.put('bbbb')
# print(B.qsize()) #返回队列里的个数
# print(B.get()) #获取队列的第一个元素
# print(B.get_nowait())

'''
 Queue.qsize() 返回队列的大小
Queue.empty() 如果队列为空，返回True,反之False
Queue.full() 如果队列满了，返回True,反之False
Queue.full 与 maxsize 大小对应
Queue.get([block[, timeout]]) 获取队列，timeout等待时间
Queue.get_nowait() 相当Queue.get(False)
Queue.put(item) 写入队列，timeout等待时间
Queue.put_nowait(item) 相当Queue.put(item, False)
Queue.task_done() 在完成一项工作之后，Queue.task_done() 函数向任务已经完成的队列发送一个信号
Queue.join() 实际上意味着等到队列为空，再执行别的操作
'''

#-----------------------------函数--------------------------------#
# def mail(user):   #定义函数名称mail def定义函数开始 user表示形参（形式参数）
#     n=123
#     n+=1
#     print(user)  #这里调用形参
#     return n  #return 定义函数规定一个返回值
# f=mail('chen')
# f=mail('Python')  #这里（）内部的就表示用户输入的实参
# print(f) # >>> chen Python  124
#
# def show(arg,xxx): #如果指定了2个形参，调用时必须输出两个形参
#     print(arg,xxx)
# show('chen','Python') #
#
# 默认参数
# def show(a1,a2=27): #a2=27 表示默认参数，默认参数必须指定在形参的最后。如果只指定了1个实参，则执行默认形参
#     print(a1,a2)
# show('chen') #>>> chen 27

# 指定参数
# def show(a1,a2):
#     print(a1,a2)
# show(a2='Python',a1='Love')  # >>> Love Python
#
# 传入列表
# def show(arg):
#     print(arg)
# show([1,2,3,4])

#动态参数
# def show(*arg): #*表示实参为元祖
#     print(arg,type(arg))
# show(1,2,3) # (1, 2, 3) <class 'tuple'>

# def show(**args): #**表示实参为字典
#     print(args,type(args))
# show(name='chen') # >>>{'name': 'chen'} <class 'dict'>  name代表字典的keys,chen代表字典的values

# def show(*arg,**args): #约定：形参*必须放在前面**放在后面
#     print(arg,type(arg))
#     print(args,type(args))
# show(1,2,3,4,name='chen') #约定：实参与形参一直
#>>>(1, 2, 3, 4) <class 'tuple'>
#   {'name': 'chen'} <class 'dict
# 注意：如果1,2,3,4为一个列表,name='chen'位一个字典比如a=[1,2,3,4] b={'name':'chen'} 实参传入时必须指定*和**,否则将列表和字典会全部写入到元组
'''
#例：
def show(*arg,**args): #约定：形参*必须放在前面**放在后面
    print(arg,type(arg))
    print(args,type(args))
a=[1,2,3,4]
b={'name':'chen'}
show(*a,**b)
# (1, 2, 3, 4) <class 'tuple'> {'name': 'chen'} <class 'dict'>
'''
#>>>
# 函数发送邮件案例
#------------------------函数测试发送邮件------------------------------#
# import smtplib
# from email.mime.text import MIMEText
# from email.utils import formataddr
# def mail(user):
#     ret = True
#     try:
#         msg = MIMEText('邮件内容：函数发送邮件测试！', 'plain', 'utf-8')
#         msg['From'] = formataddr(["武沛齐",'wptawy@126.com'])
#         msg['To'] = formataddr(["走人",'1585742649@qq.com'])
#         msg['Subject'] = "主题aaa"
#
#         server = smtplib.SMTP("smtp.126.com", 25)
#         server.login("wptawy@126.com", "WW.3945.59")
#         server.sendmail('wptawy@126.com', [user], msg.as_string())
#         server.quit()
#     except Exception:
#         ret = False
#     return ret
# ret = mail('1585742649@qq.com')
# if ret:
#     print('发送成功')
# else:
#     print('发送失败')
'''
#try案例解释
try:
    1/0
    print('OK')
except Exception:
    print('NO')
    # >>> no   如果try里的程序执行正确打印OK 否则执行except Exception里面的内容 NO
    '''
#lambda表达式
# func = lambda a: a+1
# count = func(4)
# print(count)  #>>> 5

#Python内置函数
# all() #()里指定一个序列，如果传入的所有的元素都为真，返回True，否则返回False
# #何为假 None，"",['',],(),{}
# any() #序列中只要有一个为真，返回True
# ascii() #传入一个对象时，自动执行int.__repr__() 例如print(ascii(8)) #>>> 8
# bin() #转换二进制 例：print(bin(10)) #>>> 0b1010 0b表示二进制
# bool() # 判断真假，返回True，False 例：print(bool(0)) >>> False
# bytearray() #将字符串转换为字节数组 print(bytearray('晨',encoding='utf-8')) # >>>bytearray(b'\xe6\x99\xa8')，一个汉字占3个字节
# callable() #是否可执行
# 例如：
# f=lambda x:x+1
# print(callable(f)) #>>> True f后面可以加（）代表可执行返回True
# print(callable(abs)) # 同理
# chr()把数字转换为ascii码 ord() 把ascii码转换为数字
# 例：
# print(chr(88)) #>>> X
# print(ord('X')) #>>> 88
# compile() #将字符串编译成python代码
# complex()复数
# delattr() # 反射用
# dir() #当前变量所有的key
# divmod() #取商和余数，返回元组
# enumerate() #将序列加上序号
# eval() #计算 print(eval('1+2*10+3-23')) >>> 1
# map()做条件判断操作
# map() #示例
# a=[1,2,3,4,5]
# b=map(lambda x:x+100,a) #lambda可替换为函数
# c = list(b)
# print(c) #>>>[101, 102, 103, 104, 105]
# filter() #用来过滤
# a=[1,2,3,4,5]
# b=filter(lambda x:x>4,a)
# print(list(b)) #>>> 5
# format() #调用__format__()
# frozenset() # 不能增加和修改的集合
# globals() #返回所有全局变量
# hex() #转换为十六进制 *0x表示16进制*
# locals() #局部变量
# max() #获取最大值
# min() #获取最小值
# oct() #八进制 *0o代表八进制*
# round()#四舍五入
# super()#通过子类执行父类
# vars() # 和dir()不同的是返回所有的k，val 为字典
# zip() 对应列相加
# a=['a','b','c']
# b=[1,2,3]
# b = zip(a,b)
# print(list(b)) #>>>[('a', 1), ('b', 2), ('c', 3)]


#---------------------------open文件操作---------------------#
