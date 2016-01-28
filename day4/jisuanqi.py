#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import re


def cheng(num):
    while True:
        if re.search('\d+\*\d+',num) is None:
            print('找不到乘号！')
            break
        else:
            print('调用乘函数')
            b=re.search('\d+\*\d+',num).group()
            print('匹配到%s'%b)
            bb=b.split('*')
            jieguo=float(bb[0])*float(bb[1])
            jieguo=float('%.2f'% jieguo)
            num=num.replace(b,str(jieguo))
            print(num)
    if '+' in num:
        return jia(num)
    else:return num
    # return jia(num)
def jia(num):
    print('调用加函数！')
    if '+' not in num:
        print('没有加法')
    else:
        for i in range(4):
            print(num)
            bb=re.search('[\d]?[\.]?\d+\+[\d]?[\.]?\d+',num).group()
            print(bb)
            bbb=bb.split('+')
            jieguo=float(bbb[0])+float(bbb[1])
            num=num.replace(bb,str(jieguo))
    # if '-' in num:
    return jian(num)
def jian(num):
    print('调用减函数！')
    if '-' not in num:
        print('没有减法！')
    else:
        bb=re.search('\d+\.?(\d+){0,1}\-\d+[\.]?[\d]?')
    return bb
def chu(num):
    print('调用除函数！')
    while True:
        if '/' in num:
            bb=re.search('\d+\.?(\d+?){0,1}\/\d+[\.]?[\d]?',num).group()
            print(bb)
            bbb=bb.split('/')
            jieguo=float(bbb[0])/float(bbb[1])
            jieguo=float('%.2f'% jieguo)
            num=num.replace(bb,str(jieguo))
            # print(num)
        # print(num)
        return num
def jisuan(num):
    if '/' in num:
        jieguo=chu(num)
        return jieguo
    if '*' in num:
        jieguo=cheng(num)
        return jieguo
    if '-' in num:
        jieguo=jian(num)
        return jieguo
def Search(list):
        for i in range(10):
            list = list.replace('+-','-')
            list = list.replace('++','+')
            list = list.replace('-+','-')
            list = list.replace('--','+')
            # if not re.search('\(([\+\-\*\/]?\d+){2,}\)',list):
            #     print(re.search('\(([\+\-\*\/]?\d+){2,}\)',list))
            #     print('aaa')
            #     break
            content = re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)',list).group()     # 取第一个括号里的计算值
            print('匹配到%s'%content)
            content1=content[1:len(content)-1]       # 去括号
            jieguo=jisuan(content1)
            print(jieguo)
            list=list.replace(content1,str(jieguo))
            print(list)


            print(list)
Js='1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
Js=re.sub(' ','',Js)
Search(Js)





