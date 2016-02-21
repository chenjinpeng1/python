#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
# import os,sys
# DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(DIR)
# sys.path.append(DIR)
# Read_File=open('config.txt','rb').read()
# print(Read_File)
import time,datetime
# print(time.ctime())
# print(datetime)
# a=time.strftime("%Y-%m-%d",time.gmtime())
# b=time.strftime("%Y-%m-%d",time.gmtime())
# print(a)
# print(b)
# lixi=int(a.replace('-',''))-int(time.strftime("%Y-%m-%d",time.gmtime()).replace('-',''))
# print(lixi)
# A='10'
# print(time.strptime("2016-01-28","%Y-%m-%d") )
# Curent_m=(time.strftime("%Y-%m-%d",time.gmtime()))
# print(Curent_m)
# Curent_m=Curent_m.replace(time.strftime("%m",time.gmtime()),str(int(time.strftime("%m",time.gmtime()))+1))
# Bill_time=('%s-%s'%(Curent_m,A))
# print(Bill_time)
# A='10'
# Curent_m=time.strftime("%Y-%m",time.gmtime())
# Curent_m=Curent_m.replace(time.strftime("%m",time.gmtime()),str(int(time.strftime("%m",time.gmtime()))+1))
# Bill_time=('%s-%s'%(Curent_m,A))
# print(Bill_time)
# a=9999.999999999998
# b=float('%.3f' %a)
# print(a)
# print(b)
d=10000
b=-2000
c=0
# for i in range(30):
#     a=b*0.0005
#     a=float('%-7.3f'%a)
#     c+=a
#     b+=a
#     d+=a
#     print(a)
#     print(b)
#     print(d)
#     print('---------------------')
# b=float('%.3f'%b)
# c=float('%.3f'%c)
# d=float('%.3f'%d)
# print(b)
# print(c)
# print(d)
# Curent_m=(time.strftime("%Y-%m-%d",time.gmtime())) #当前时间
# print(Curent_m)
# import pickle,os,sys
# DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(DIR)
# print(DIR)
# A='%s%s'%(DIR,'\Card\config.txt') #读取config.txt文件
# print(A)
# B='%s%s'%(DIR,'\Card\X.txt') #读取xiaofei文件
# print(B)
# C='%s%s'%(DIR,'\Card\caozuo_log.txt') #读取caozuo_log.txt文件
# print(C)
import collections
log=collections.defaultdict(list)

# print(a)
# log['1']=[1,2,3,4]
# print(log)
# print(len(log['1']))
# for i in range(len(log['1'])):
#     print('aaa')
# import pickle,datetime
# File=open('caozuo_log.txt','rb')
# info=pickle.loads(File.read())
# File.close()
# print(info['root'][0])
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())) #将struct_time格式转成指定的字符串格式)
print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()))