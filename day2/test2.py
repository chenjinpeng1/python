##########################int##########################
# Num = 2
# B = [1,2,3,4,5,6]
# #绝对值
# A = Num.__abs__()
# print (A) #==7
# A = Num.__add__(3)  #两个int相加 等同于X+Y
# print (A)   # ==10
# A = Num.__and__(14)
# # 7 = 0000 0111
# # 14 = 0000 1110
# # 等同于 7&14 = 6
# print (A) # ==6
# Num.__cmp__(8) #等同于a>b 或者a<b 判断a和b的大小
# Num.__coerce__(self,y) == coerce(x,y)# 返回元组 3.0取消
# A = Num.__divmod__(2) # = divmod(x,y)取7/2的商和余,组成元组
# print (A) # = （3,1）
# A = Num.__float__()  #转换浮点型 == float(Num)
# print (A)
# A = Num.__floordiv__(3) # = 7//3 只取商
# print (A)  # =2
# Num.__getattribute__('aaa') #反射会用
# A = Num.__getnewargs__() #内部调用 __new__方法或创建对象时传入参数使用
# print (type(A),A) #= 78

##########################字符串##########################
#首字母大写
Name = 'chen'
# A = Name.capitalize()
# print (A)
#内容居中，width：总长度；fillchar：空白处填充内容，默认无
# A = Name.center(20,'#')
# print (A)
#查找字符串出现次数0,10表示从0到10个字符，不加默认为全部字符
# Name = 'aabbbbb2222ddddsaaadffffsss'
# A = Name.count('a',0,10)
# print (A)
#编码转换
# Name= "陈金彭"
# A = Name.encode('gbk')
# print(A)
#判断字符串是否已某个字符串结尾，0,3代表在第0-3个字符去匹配，可取消
# A = Name.endswith('e',0,3)
# print (A)
#将tab键转换为空格，默认为8个空格
# Name = 'ch\ten'
# A = Name.expandtabs(tabsize=100)
# print (A)
# #需找字符串所在的索引位置，没找到返回-1，从第十个字符串开始-第16个字符串
# Name = 'abcaaaahhhhbbbbcccc'
# A = Name.find('c',10,16)
# print (A)
#字符串格式化
# Name = "陈金彭"
# Age = 17
# print ('My Name is {0},Age is {1}'.format(Name,Age))
#查找字符串所在的位置，不存在则报错
# A = Name.index('g')
# print (A)
#匹配字符串是否为字母或者数字，返回True False
# A = Name.isalnum()
# print (A)
#匹配是否为字母,
# Name = '111'
# A = Name.isalpha()
# print (A)
# #匹配是否为数字
# A = Name.isdigit()
# print (A)
# #匹配是否小写
# A = Name.islower()
# print (A)
#是否有空格
# Name = '   '
# A = Name.isspace()
# print (A)
#是否有标题,标题：（首字母必须大写，如有空格其次首字母必须大写）
# Name = 'Aaad Aa'
# A = Name.istitle()
# print (A)