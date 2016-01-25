#python 3.5环境,解释器在linux需要改变
#商城购物，阅读手册查询readme文件
#调用文件 login.txt,lock.txt
#作者：S12-陈金彭
# def test():
#     print('学习函数！')
# test()
# test2=test()
# test2
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
#-------------------------------------------------------------参数
# def show(a1):
#     print(a1)
# show(111)
#-------------------------------------------------------------默认参数
# def show(a1,a2='Hello'):
#     print(a1,a2)
# show(111)
#-------------------------------------------------------------指定参数
# def show(a1,a2):
#     print(a1,a2)
# show(a2=111,a1=222)
#-------------------------------------------------------------动态参数
# def show(*aa):  # *代表元组
#     print(aa,type(aa))
# show(1,2,3,4,'aa')
# def show (*aa,**aaa):# **代表字典
#     print(aa,aaa,type(aa),type(*aaa))
# show(1,2,3,aa='bb')

#如果想把一个列表和一个字典放入形参，转换为同等实参，需在传入实参加上等同的*号
#例如：
# def show(*a,**aa):
#     print(a,aa)
# a=[1,2,3]
# b={'1':1,'2':2,'3':3}
# show(*a,**b)

#--------------------------format格式化输出，输出条件包含列表，元祖-------------------------------------

# s1 = '{0} is {1}'
# aa = s1.format(1,1)
# print(aa)

# s2='{0} is {1}'
# l=[1,1]
# ab=s2.format(*l)
# print(ab)

# s3='{name} is {age}'
# l = {'name':chen,'age':27}
# ac=s3.format(**l)
# print(ac)
#----------------------------------lambda表达式，简单函数的表示方式
# func=lambda  a:a+1
# #创建形式参数a
# #函数内容，a+1  并把结果return
# ret = func(100)
# print(ret)

#---------------------------------python内置函数-------
# all() #判断
# print(all([]))
# print(all('1'))
# any()
# print(ascii('撒'))  #将
#bin()
# print(all([1,2,3,4]))
# print(all((1,2,3,4)))
#print(bool([1,])) #判断列表，字典 字符串 数字等True and False


# ---------------------------------------------------
# eval()进行计算
# filter,map
#     filter #根据条件进行筛选
#     map
# li = [11,22,33,44] #要求 每个元素加100
# new_li= map(lambda x:x+100,li)
# print(list(new_li))
# li = [11,22,33,44] #需求，筛选出大于33的数字
# def func(x):
#     if x > 33:
#         return  True
#     else:
#         return False
# a = filter(func,li)
# a = list(a)
# print(a)

# hex()#禁止转换
# print(globals()) #全局变量
# print(locals()) #本地变量
# print(max(1,2,3333333333)) #取最大值
# min(1,2,33333333) #取最小值
# repr()#返回一个机器识别的字符串
# print(round(2.3)) #返回整数
# dir()#返回所有的key
vars()#返回变量的所有k,val
# zip#两个列表中的索引值对应相加
# x=[1,2,3]
# y=[4,5,6]
# a = zip(x,y)
# for i in a:
#     print(i)

# print(oct())#返回数字的八进制
# read 按照字符读取 tell 按照字节去找,用来查看当前指针位置
# f = open('test.log','r')
# for i in f.read():
#     print(f.tell())
#     print(i)
# f.truncate()  #按照指针的位置截取指针前面的内容
import json
a = '{"k1":"v1"}'
b = a.join(a)
print(b)
