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
# #是否全部为大写，返回True；否则返回False
# Name='CHEN'
# A = Name.isupper()
# print (A)
#判断是否为十进制字符，返回True
# Name = '123'
# A=Name.isdecimal()
# print (A)
# #判断是否只有数字字符 返回True
# Name = '123'
# A=Name.isnumeric()
# print (A)
#字符串拼接‘’.join()
# A = '陈'
# B = '金彭'
# print(''.join([A,B]))
# #返回字符串左对齐，填充符号（5表示算是chen4个字符串，因此只会填充一个#号）
# A = Name.ljust(5,'#')
# print (A)
#返回的字符串转换为小写
# Name='CHEN'
# A = Name.lower()
# print (A)
# #去除字符串左边的空格
# Name='   chenjin  peng  '
# A = Name.lstrip()
# print (A)

####maketrans以及translate方法解释：
#Python maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。注：两个字符串的长度必须相同，为一一对应的关系。
#Python translate() 方法根据参数table给出的表(包含 256 个字符)转换字符串的字符, 要过滤掉的字符放到 del 参数中。
# A='abcde'
# B='12345'
# AA = str.maketrans(A,B)
# CC='my name is chen...abe'
# print(CC.translate(AA))

#将字符串转换为全大写（字符串：ASCII字符）
# A = Name.upper()
# print (A)
#字符串以制定字符分割为元祖
# A=Name.partition('e')
# print(type(A))
#replace替换字符串
# A=Name.replace('h','a')
# print (A)
#Python rindex() 返回子字符串 str 在字符串中最后出现的位置，如果没有匹配的字符串会报异常，可制定字符串的起始以及结束的索引值
# A=Name.rfind('n',0,4)
# print(A)
#返回字符串最后一次出现的位置，如果没有匹配项则返回-1
# A=Name.rindex('c')
# print (A)
#Python rjust() 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串
# A=Name.rjust(5,'#')
# print (A)
