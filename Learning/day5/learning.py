#python 3.5环境,解释器在linux需要改变
#作者：S12-陈金彭
#re
import re
# phone_str = "hey my name is alex, and my phone number is 13651054607, please call me if you are pretty!"
# phone_str2 = "hey my name is alex, and my phone number is 18651054622, please call me if you are pretty!"
#
# m = re.search("(1)([358](\d){9})",phone_str2)
# print(m)
# if m:
#     print(m.group())
# ip_addr = "inet 192.168.60.223 netmask 0xffffff00 broadcast 192.168.60.255"
#
# m = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip_addr)
#
# print(m.group())
# contactInfo = 'Old_boy_School, BeijingChangpingShahe: 010-8343245'
# # match = re.search('\w+, \w+: \S+', contactInfo)
# match = re.search(r'(?P<last>\w+), (?P<first>\w+): (?P<phone>\S+)', contactInfo)
# print(match.group())
# email = "alex.li@126.com   http://www.oldboyedu.com"

# m = re.search(r"[0-9.a-z]{0,26}@[0-9.a-z]{0,20}.[0-9a-z]{0,8}", email)
# print(m.group())
# num = [10,4,33,21,565,226,777,11,2,44,666]
# for i in range(1,len(num)):
#     for ii in range(len(num)-i):
#         if num[ii] > num[ii+1]:
#             tmp = num[ii]
#             num[ii] = num[ii+1]
#             num[ii+1] = tmp
# print(num)
# count = 0
# data = [10,4,33,21,54,3,8,11,5,22,2,1,17,13,6]
# for i in range(len(data) - 4):
#     for j in range(len(data) - i -1):
#         if data[j] > data[j+1]:
#             data[j], data[j+1] = data[j + 1], data[j]
#             count += 1
#             print(data)
#     count += 1
# print(data)
# print(count)


#===================================   time模块
# import time
# import datetime
# # print(time.time())
# print(time.ctime(11111111111))
# print(time.ctime(time.time()-10))
# print(time.gmtime(time.time()-5))
# print(time.gmtime(time.time()-10))

##################################  random模块
import random
# print(random.randrange(1,10)) #生成小数



# aa=''
# for i in range(10):
#     num = random.randrange(0,9)
#     if num != i:
#         tmp= chr(random.randint(65,90))
#     else:
#         tmp = random.randint(0,9)
#     aa+=str(tmp)
# print(aa)
# import random
# print(random.random)
# aa=random.randrange(0,10)
# print(aa)
# checkcode = ''
# for i in range(7):
#     current = random.randrange(0, 10)
#     if current != i:
#         temp = chr(random.randint(65,90))
#     else:
#         temp = random.randint(0,9)
#     checkcode += str(temp)
# print (checkcode)
# func = lambda a,b:a+1
# aa=func(99,'aaaaa')
# data = [10,4,33,21,54,3,8,11,5,22,2,1,17,13,6]
# print("before sort:",data)
# count = 0
# for j in range(1,len(data)):
#     tmp = 0
#     for i in range(len(data)-j):
#         if data[i] > data[i+1]:
#             tmp=data[i]
#             data[i] = data[i+1]
#             data[i+1] = tmp
#             count+=1
#             # print(count)
#     # count+=1
#     # print(count)
#     # print(data)
# print("after sort:",data)
# print(count)

# import sys
# import time
# for i in range(10):
#     sys.stdout.write('#')
#     sys.stdout.flush()
#     time.sleep(0.3)
import pickle
f = open('test.txt','wb')
info = {
    'chen':'123',
    'alex':'456',
}
f.write(pickle.dumps(info))
f.close()
































