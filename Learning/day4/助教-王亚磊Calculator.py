#-*- coding:utf-8 -*-
#/usr/bin/env python
import re
string ='1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
#格式化表达式中的 + - 剔除表达式中的空格
def format_add_sub(string):
    #剔除空格
    string = re.sub('\s*','',string)
    #负负为正 “--” = “+”
    string = string.replace('--','+')
    #负正为负 “-+” = “-”
    string = string.replace('-+','-')
    #正负为负 “+-” = “-”
    string = string.replace('+-','-')
    #正正为正 “++” = “+”
    string = string.replace('++','+')
    #return格式化后的表达式
    return string
#计算乘除
def mul_div(string):
    #调用格式化表达式方法format_add_sub（）对表达式进行格式化
    string = format_add_sub(string)
    #如果不存在匹配的表达式（即不包含乘除）则return返回string
    if not re.search('\d+\.?\d*[\*\/]+[\+\-]?\d+\.?\d*',string):
        return string
    #检索第一个乘除表达式
    s = re.search('\d+\.*\d*[\*,\/]+[\+\-]?\d+\.*\d*',string).group()
    #判断检索到的表达式是 乘 或 除 并交给相应的程序进行处理
    #如果为乘
    if re.search('\*',s):
        #以乘号为分隔符进行分割 并 对分割后的值进行浮点格式化、乘法运算
        resuit = float(s.split('*')[0])*float(s.split('*')[1])
        #对表达式中的元素进行替换，将计算结果替换对应的程式
        string = string.replace(s,str(resuit),1)
    elif re.search('/',s):
        #以除号为分隔符进行分割 并 对分割后的值进行浮点格式化、除法运算
        resuit = float(s.split('/')[0])/float(s.split('/')[1])
        #对表达式中的元素进行替换，将计算结果替换对应的程式
        string = string.replace(s,str(resuit),1)
    #对方法进行迭代计算 并return返回计算的结果
    return mul_div(string)
#计算加减
def add_sub (string):
    #调用格式化表达式方法format_add_sub（）对表达式进行格式化
    string = format_add_sub(string)
    #如果不存在匹配的表达式（即不包含加减）则return返回string
    if not re.search('\d+\.?\d*[\+\-]\d+\.?\d*',string):
        return string
    #检索第一个加减表达式
    s = re.search('\-?\d+\.*\d*[\+,\-]\d+\.*\d*',string).group()
    if re.search('\+',s):
        #以“+”号为分隔符进行分割 并 对分割后的值进行浮点格式化、加法运算
        resuit = float(s.split('+')[0])+float(s.split('+')[1])
        #对表达式中的元素进行替换，将计算结果替换对应的程式
        string = string.replace(s,str(resuit),1)
    elif re.search('-',s):
        #以“-”号为分隔符进行分割 并 对分割后的值进行浮点格式化、减法运算
        resuit = float(s.split('-')[0])-float(s.split('-')[1])
        #对表达式中的元素进行替换，将计算结果替换对应的程式
        string = string.replace(s,str(resuit),1)
    #对方法进行迭代计算 并return返回计算的结果
    return add_sub(string)
def compute(string):
    #计算乘除
    string = mul_div(string)
    #计算加减
    string = add_sub (string)
    #返回值
    return string
def remove_bracket (string):
    #调用格式化表达式方法format_add_sub（）对表达式进行格式化
    string = format_add_sub(string)
    #如果未检索到括号 则 return 计算结果
    if not re.search('\(([\+\-\*\/]*\d+\.*\d*){1,}\)',string):
        return compute(string)
    #检索内层括号
    s = re.search('\(([\+\-\*\/]*\d+\.*\d*){2,}\)',string).group()
    #剔除掉表达式的括号便于计算
    ds = s.strip('\(\)')
    #将括号内的表达式交给计算程序进行计算
    resut = compute(ds)
    #将计算出的结果替换掉该括号表达式
    string = string.replace(s,resut,1)
    #迭代执行括号剥离方法、计算出括号内的结果、将结果替换掉原表达式
    return remove_bracket (string)
if __name__ == '__main__':
   print remove_bracket (string)