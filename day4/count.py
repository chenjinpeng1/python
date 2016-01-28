#python 3.5环境，解释器在linux需要改变
#作者：S12-陈金彭
import re
# def Count(num):
#     b=[num,]
#     bb=re.search('([\-|\/|\*]?\d+){4,}',b[0]).group()
#     bbb=bb.split('*')
#     print(bbb,bb)
#     if '/' in bb:
#         jieguo=int(bbb[0])/int(bbb[1])
#         print(jieguo)
# a='(9-2*5/3+7/3*99/4*2998+10*568/14)'
# for i in range(10):
#     if re.search('\d+\*\d+',a) is None:
#         break
#     b=re.search('\d+\*\d+',a).group()
#     bb=b.split('*')
#     if '*' in b:
#         jieguo=int(bb[0])*int(bb[1])
#         print(jieguo)
#         a=a.replace(b,str(jieguo))
#     print(a)
# a='(9-10/3+7/300/42998+10*568/14)'
# a=[a,]
# b=re.search('((\d+)[\*]\d+)',a[0]).group()
# print(b)
# print(a)
# A,B,C=re.split('((\d+)[\*]\d+)',a,1)
# print(B)
# a='1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
# a=re.sub(' ','',a)
# print(a)
# a=[a,]
# print(a)
# b=re.search('\(([\+\-\*\/]?\d+){2,}\)',a[0]).group()
# print(b)
# A,B,C=re.split(b,a[0],maxsplit=1)
# print(A)
# print(C)
#a=''\d+\*\d+''
# a='9-3.33+0.02/11992.0+5680.0/14'
# for i in range(5):
#     content = re.search('\d+\.?(\d+?){1,}\/\d+\.?(\d+?){1,}',a).group()
#     print(content)
#     a=a.replace(content,'aaa')
#     print(a)
a='-8.0'
print(float(a))
if int(float(a)) is True:
    print(1111111)
