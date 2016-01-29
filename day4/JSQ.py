#python 3.5环境，解释器在linux需要改变
#作者：S12-陈金彭
import re
def jisuan(num):
    num=chengchu(num)
    # String=jiajian(num)
    return num
def chengchu(num):
    if not re.search('\-?\d+[\.?\d+]?[\*|\/]?\d+',num):
        return num
        # print(re.search('\-?\d+[\.?\d+]?[\*|\/]?\d+',num))
    String=re.search('\-?\d+[\.?\d+]?[\*|\/]?\d+',num).group()
    if '/' in String:
        b='%.2f'%(float(re.split('\/',String)[0])/float(re.split('\/',String)[1]))
        print('计算结果：%s'%b)
        num=num.replace(String,str(b))
    elif '*' in String:
        b='%.2f'%(float(re.split('\*',String)[0])*float(re.split('\*',String)[1]))
        print('计算结果：%s'%b)
        num=num.replace(String,str(b))
    print(num)
    # return chengchu(num)
def jiajian(num):
    pass
def Sreach(num):
    String=re.search('\(([\+\-\*\/]?\d+){2,}\)',num).group()
    String_1=String.strip('\(|\)')
    print('匹配到%s'%String_1)
    jieguo=jisuan(String_1)
    num=num.replace(String,str(jieguo))
    num=num.replace('+-','-')
    print(num)
    return Sreach(num)
Input='1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
print(Input)
String=Input.replace(' ','')
Sreach(String)