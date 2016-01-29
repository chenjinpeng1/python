#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import re
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
    while True:
        if '-' not in num:
            print('没有减法！')
        else:
            bb=re.search('\-?\d+\.?(\d+){0,1}\-\d+[\.]?[\d]?',num)
    return bb
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
    return num
def chu(num):
    print('调用除函数！')
    while True:
        if '/' in num:
            bb=re.search('\d+\.?(\d+?){0,1}\/\d+[\.]?[\d]?',num).group()
            print(bb)
            bbb=bb.split('/')
            jieguo=float(bbb[0])/float(bbb[1])
            jieguo=float('%.2f'%jieguo)
            num=num.replace(bb,str(jieguo))
        else:break
    return num
def Search(list):
    for i in range(10):
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
        content1=content[1:len(content)-1]       # 去括号
        try:
            if type(float(content1)) is float:
                print('aaaaaaaaaaa')
                list=list.replace(content,str(content1))
        except Exception:
            print('aaaaa')
        if '*' in content1:
            jieguo=cheng(content1)
            print('计算后结果是%s'%jieguo)
            list=list.replace(content1,str(jieguo))
        elif '/' in content1:
            jieguo=chu(content1)
            print('计算后结果是%s'%jieguo)
            list=list.replace(content1,str(jieguo))
        elif '-' in content1:
            jieguo=jian(content1)
            print('计算后结果是%s'%jieguo)
            list=list.replace(content,str(jieguo))

        print(list)
Js='1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
Js=re.sub(' ','',Js)
Search(Js)





