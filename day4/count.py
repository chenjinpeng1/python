# #-*- coding:utf-8 -*-
# #/usr/bin/env python
# import re
# string ='1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
# def format_add_sub(string):
#     string = re.sub('\s*','',string)
#     string = string.replace('--','+')
#     string = string.replace('-+','-')
#     string = string.replace('+-','-')
#     string = string.replace('++','+')
#     return string
# #计算乘除
# def mul_div(string):
#     #调用格式化表达式方法format_add_sub（）对表达式进行格式化
#     string = format_add_sub(string)
#     if not re.search('\d+\.?\d*[\*\/]+[\+\-]?\d+\.?\d*',string):
#         return string
#     s = re.search('\d+\.*\d*[\*,\/]+[\+\-]?\d+\.*\d*',string).group()
#     if re.search('\*',s):
#         resuit = float(s.split('*')[0])*float(s.split('*')[1])
#         string = string.replace(s,str(resuit),1)
#     elif re.search('/',s):
#         resuit = float(s.split('/')[0])/float(s.split('/')[1])
#         string = string.replace(s,str(resuit),1)
#     return mul_div(string)
# #计算加减
# def add_sub (string):
#     string = format_add_sub(string)
#     if not re.search('\d+\.?\d*[\+\-]\d+\.?\d*',string):
#         return string
#     s = re.search('\-?\d+\.*\d*[\+,\-]\d+\.*\d*',string).group()
#     if re.search('\+',s):
#         resuit = float(s.split('+')[0])+float(s.split('+')[1])
#         string = string.replace(s,str(resuit),1)
#     elif re.search('-',s):
#         resuit = float(s.split('-')[0])-float(s.split('-')[1])
#         string = string.replace(s,str(resuit),1)
#     return add_sub(string)
# def compute(string):
#     string = mul_div(string)
#     string = add_sub (string)
#     return string
# def remove_bracket (string):
#     string = format_add_sub(string)
#     if not re.search('\(([\+\-\*\/]*\d+\.*\d*){1,}\)',string):
#         return compute(string)
#     s = re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)',string).group()
#     ds = s.strip('\(\)')
#     resut = compute(ds)
#     string = string.replace(s,resut,1)
#     return remove_bracket (string)
# if __name__ == '__main__':
#    print (remove_bracket (string))
import re
def aa(aa):
    if  re.search('\-?\d+[\.?\d+]?[\*|\/]?\d+',a) is None:
        return aa
a='-8'
b=aa(a)
print(b)