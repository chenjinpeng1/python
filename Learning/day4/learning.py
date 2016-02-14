#python 3.5环境,解释器在linux需要改变
#商城购物，阅读手册查询readme文件
#作者：S12-陈金彭
# li = [13, 22, 6, 99, 11]
# for i in range(1,5):
#     for m in range(len(li)-i):
#         if li[m] > li[m+1]:
#             temp = li[m+1]
#             li[m+1] = li[m]
#             li[m] = temp
# print(li)
#---------------------------迭代器-----------------------#
# name = iter(['chen','a','b','c'])
# print(name.__next__())
# print(name.__next__())
# print(name.__next__())
# print(name.__next__())
# print(name.__next__()) #最后一次会报错
# def cash_money(money,num):
#     while money > 0:
#         money-=num
#         yield num,money
#         print('又来取钱了啊，败家子！！')
# atm=cash_money(1000,200)
# print('取了%s,还剩下%s'%atm.__next__())
# print('取了%s,还剩下%s'%atm.__next__())
# print('交个大保健')
# print('取了%s,还剩下%s'%atm.__next__())
# print('取了%s,还剩下%s'%atm.__next__())

# import time
# def chi(name):
#     print('%s 来买包子了！'%name)
#     while True:
#         baozi = yield
#         print('包子 %s 来了，被%s 吃了！'%(baozi,name))
# def zuo(name,name2):
#     A=name
#     B=name2
#     c = chi(A)
#     c2 = chi(B)
#     c.__next__()
#     c2.__next__()
#     print('老子开始准备做包子了！')
#     for i in range(1):
#         time.sleep(1)
#         print('做了两个包子！')
#         c.send(i)
#         c2.send(i)
# zuo('chen','qiu')
# def chi(name,num):
#     print('%s来买包子,买%s个'%(name,num))
#     while True:
#         baozi = yield
#         print('包子%s来了，被%s吃了'%(baozi,name))
# def zuo(name,name2):
#     A=chi(name,10)
#     B=chi(name2,10)
#     A.__next__()
#     B.__next__()
#     print('老子开始做包子了')
#     for i in range(1,20,2):
#         print('做了两个包子！')
#         A.send(i)
#         B.send(i+1)
# zuo('陈','邱')
# def login(func):
#     if 1==1:
#      print('passed user verification...')
#      return func
#     else:
#         return aa
# def tv(name):
#     print('欢迎来到%s!'%name)
# def aa(aa):
#     print('aaaaa')
# tv = login(tv)
# tv('Tv')


#-----------------------装饰器
# def login(func):
#     def inner(arg):
#         print('passwd user verification')
#         func(arg)
#     return inner
# @login
# def tv(name):
#     print('Welcome %s to tv page!!'%name)
# tv('tv')
# #tv = login(tv)('tv')

#-----------------------------

# def Before(request,kargs):
#     print ('before')
# # print(Before(1,2))
# def After(request,kargs):
#     print ('after')
# def Filter(before_func,after_func):
#     def outer(main_func):
#         def wrapper(request,kargs):
#             before_result = before_func(request,kargs)
#             # if(before_result != None):
#             #     return before_result;
#             main_result = main_func(request,kargs)
#             # if(main_result != None):
#             #     return main_result;
#             after_result = after_func(request,kargs)
#             # if(after_result != None):
#             #     return after_result;
#         return wrapper
#     return outer
# @Filter(Before, After)
# def Index(request,kargs):
#     print ('index')
# if __name__ == '__main__':
#     Index(1,2)    #Filter(Before,After)(Index)('1','2')
#                                 #outer (Index)('1','2')
#                                      #wrapper ('1','2')
#                                            #Before(1,2)
#                                             #Index(1,2)
#                                             #After(1,2)
 u



# def w1(func):
#     def inner(*args,**kwargs):
#         # 验证1
#         # 验证2
#         # 验证3
#         print('yz1')
#         return func(*args,**kwargs)
#     return inner

# def w2(func):
#     def inner(*args,**kwargs):
#         # 验证1
#         # 验证2
#         # 验证3
#         print('yz2')
#         return func(*args,**kwargs)
#     return inner
#
#
# @w1
# @w2
# def f1(arg1,arg2,arg3):
#     print ('f1')
# f1(1,2,3)
#-----------------------------迭代器
# def calc(n):
#     print(n)
#     if n/2 >1:
#         res = calc(n/2)
#         print('res',res)
#         # return calc(n/2)
#     print('N',n)
#     return n
# calc(10)

#--------------斐波那契数列-----------------#
# def func(a,b,c):
#     if a == 0:
#         print(a,b)
#     d=a+b
#     print(d)
#     if d < c:

#         func(b,d,c)
# func(0,1,50)
#----------------------二分法------------------#

# def func(yuan,find):
#     zhongjian = int(len(yuan) / 2)
#     if len(yuan) >=1:
#         if yuan[zhongjian] > find:
#             func(yuan[:zhongjian],find) #func(yuan[:zhongjian],find)
#         elif  yuan[zhongjian] < find:
#             func(yuan[zhongjian:],find)
#         else:
#             print('found find',yuan[zhongjian])
#     else:
#         print('no found')
# data = list(range(1,600,1))
#
# func(data,480)

'''
2分算法思路：
1、func(data,8)调用函数func 传入的实参为data列表，8
2、执行函数体， 此时zhongjian函数的值就等于列表data的长度/2 ， 假设为300
3、进行判断此时yuan长度>=1 数据是否还有值，这里等于设置了2分算法的条件
4、进入判断，原数据的中间值是否比查找的值大， 这里暂定300 > 8 , 因此进入了第一次判断进行的操作
5、再次执行函数func(yuan[:zhongjian],find) 此时函数体里第一个形参就=600[:300] 大于索引往左切片
6、之后进行依次循环 如果循环到yuan[zhongjian] < find 则执行<判断里面的函数体知道判断结束
'''
# a=[[i for i in range(4)] for ii in range(4) ]
# for i in a:
#     print(i)
'''
[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3]
'''
# a=[[i for i in range(4)] for ii in range(4) ]
# for i in range(len(a)):
#     for ii in range(len(a)):
#         a[i][ii]=[i]
#     print(a[i])

# data = [[col for col in range(4)]  for row in range(4)]
# for i in range(len(data)):
#     a = [data[i][i] for row in range(4)]
#     print(a)

# a=[[i for i in range(4)] for ii in range(4)]
# print(a)
