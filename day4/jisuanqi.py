#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import re
import operator
Js='1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
Js=re.sub(' ','',Js)
Js_list=[Js,]
print(Js_list)
content = re.search('\(([\+\-\*\/]?\d+){2,}\)',Js_list[0]).group()
print(content)
before,nothing,after=re.split('\(([\+\-\*\/]?\d+){2,}\)',Js_list[0],1)
content=content[1:len(content)-1]
print(content)
print(Js_list)