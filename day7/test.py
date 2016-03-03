#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import sys,hashlib,os,subprocess
# os.chdir('C:/Users/chen/PycharmProjects/python/day7/chen')
# print(os.getcwd())
# a=os.path.join(os.getcwd(),)
# b=os.getcwd()
# print(b)
# a=os.chdir("./")
# print(os.getcwd())
# cmd_call = subprocess.Popen("rename chen chen1",shell=True) # 将读取到的命令通过管道符进行输出到变量
# cmd_result = cmd_call.stdout.read()
# print(cmd_call)
'''
aaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaa
aaaaaaaaaaaa
aaaaaaaaaaaa
aaaaaaaaaaaa
'''
# file = input(">>>:")
# AA=os.path.isfile(file)
# print(AA)
# if AA is not True:
#     print("wocao")
# if A is not True:
#     print(A)
# else:
#     print("exit")
A=os.stat("作业思路分析.txt")
print(A.st_size)