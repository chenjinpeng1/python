#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import re

def cheng(num):
    print('调用乘函数')
    while True:
        if re.search('\d+\*\d+',num) is None:
            print('找不到乘号！')
            break
        else:
            b=re.search('\d+\*\d+',num).group()
            bb=b.split('*')
            jieguo=int(bb[0])*int(bb[1])
            num=num.replace(b,str(jieguo))
            print(num)
    # num='(%s)'%num
    return num

def chu(num):
    for i in range(4):
        if '/' in num:
            print(num)
            bb=re.search('[\-|\d]?\d+\/\d+',num).group()
            print(bb)
            bbb=bb.split('/')
            jieguo=int(bbb[0])/int(bbb[1])
            num=num.replace(bb,str(jieguo))
            print(num)
        else:break
    return num
def Search(list):
    for i in range(4):
        list = list.replace('+-','-')
        list = list.replace('++','+')
        list = list.replace('-+','-')
        list = list.replace('--','+')
        if not re.search('\(([\+\-\*\/]?\d+){2,}\)',list):
            print(re.search('\(([\+\-\*\/]?\d+){2,}\)',list))
            print('aaa')
            break
        content = re.search('\(([\+\-\*\/]?\d+){2,}\)',list).group()     # 取第一个括号里的计算值
        print('匹配到%s'%content)
        # # A,B,C=re.split('\(([\+\-\*\/]?\d+){2,}\)',list,maxsplit=1)
        content1=content[1:len(content)-1]       # 去括号
        if '*' in content1:
            jieguo=cheng(content1)
            list=list.replace(content1,str(jieguo))
        if '/' in content1:
            jieguo=chu(content1)
            list=list.replace(content1,str(jieguo))
        # if '*' in content1:
        #     jieguo=cheng(content1)
        #     list=list.replace(content,str(jieguo))
        print(list)
        # list=('%s%s%s'%(A,jieguo,C))
Js='1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
Js=re.sub(' ','',Js)
Search(Js)





