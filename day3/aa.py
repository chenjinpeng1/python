#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
def add(backend):
    backend_title = 'backend %s\n' % backend                      #查找对应的backend
    with open('ha.txt','r') as f:  #把老文件写到新文件里,然后在新文件里做修改
        global  flag
        flag = True
        for line in f.readlines():
            if line == backend_title:
                print("找到了")
                flag = False
                break
                #f_write.write("\n" + "%s" % backend_server_add)
            #
        if flag:
            print("没找到对应的backend")
a = input("input:")
add(a)



