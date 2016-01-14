#python 3.5环境，解释器在linux需要改变
#用户登陆认证，阅读手册查询readme文件
#调用文件 login.txt,lock.txt
#作者：S12-陈金彭
Auth_File="login.txt"                               #认证登陆文件
Lock_File="lock.txt"                                #锁定文件
F_Auth = open(Auth_File)
Read_Auth=F_Auth.readlines()                          #执行前将账号密码文件读取到变量，避免循环读取
F_Auth.close()
User_Exit=[]
while True:
    LoginSusses=False                               #循环开始前先定义登陆成功失败的变量。方便循环嵌套跳转
    count = 0                                        #定义计数器，错误三次锁定
    Read_Lock=open(Lock_File)                        #读取锁文件到变量Lock_List
    Lock_List=[]
    for i in Read_Lock.readlines():
        line = i.strip('\n')
        a = Lock_List.append(line)
    Read_Lock.close()
    Name=input('请输入你的账户:').strip()
    for i in Read_Auth:
        i = i.split()
        User_Exit.extend(i[0].split())
    if Name not in User_Exit:
        print ('你输入的用户名不存在，请重新输入')
        continue
    if Name in Lock_List:
        A=input("你的账户已经被锁定！！请联系管理员解锁！输入Y解锁，任意键退出:")             #，用户登陆前先判断用户是否被锁定后在进行密码判断。
        if A == 'Y':
            f = open('lock.txt')
            line = f.read()
            b = line.replace("%s\n"%Name,"")
            f = open("lock.txt","w")
            f.write(b)                                                                          #解锁用户，先将文件内容读出到内存，之后将解锁的用户名替换掉在写入即可。以下是2种方式
            print ("锁定已解除，请继续输入密码")
        else:break
    for line in Read_Auth:
        line = line.split()
        if Name in line:
            for i in range(3):                              #定义3次循环，
                Passwd=input('请输入你的密码：')
                if Passwd == line[1]:
                    LoginSusses=True
                    print ("Good，欢迎您登陆：%s" %Name)
                    break
                else:
                    print ("你的密码错误，请重新输入")
                    count +=1                                       #每次密码错误后计数器count+1,3次后锁定，写入锁文件
                if count == 3:
                    f = open(Lock_File,'a')
                    f.write('%s\n'%Name)
                    f.close()
                    print ("你的密码错误次数达到3次，已被锁定")
        if LoginSusses is True:break                                #跳出2层循环
    if count ==3:                                                     #锁定用户后跳出2层循环
        break
    if LoginSusses is True:                                             #跳出2层循环
        break