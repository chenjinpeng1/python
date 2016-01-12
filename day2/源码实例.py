##########################int##########################
# bit_length()
# bit_length()返回表示该数字的时占用的最少位数
# 语法：int.bit_length()
# Num=15  #15,(8 4 2 1) 0000 1111 占4位
# A=Num.bit_length()
# print(A)
#
# abs()
# print (abs(-15)) #绝对值 引用int.__abs__()
#
# Num=15
# + 加号
# A=Num.__add__(15)  #等同于15+15
# print (A)
#
# A=Num.__and__(14) #与运算 等同于&符号 15&14
# print(A)
#
# A=Num.__bool__() #等同于 Num != 0 返回True和False
# print(A)
#
# A=Num.__divmod__(10) #等同于15/10，区别在于返回元组
# print(A)
# print (15/10)
#
# A=Num.__floordiv__(10) #和divmod区别在于 floordiv只取商
# print(A)
# print(15//10)
#
# A=Num.__getattribute__() #反射用
# print(A)
#
# A=Num.__getnewargs__() #内部调用 __new__方法或创建对象时传入参数使用
# print(A)
#
#
#
# int.__index__( ) #index，是当前对象如果作为某个序列的 索引 时，自动会执行该对象的 __index__ 方法，将其返回值作为 索引
# x=[1,2,3,4,5,6,7]
# y=5
# z=1
# A=x[z:y]
# print(A)
#
# int.__invert__() #操作符进行的取反行为
#
# int.__pow__() #次幂
# A=Num.__pow__(2) #等同于pow(15,2)
# print(A)
#
# A=Num.__repr__() #将数字转换为字符串
# print(type(A))






















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
# Python capitalize()
# Python capitalize()将字符串的第一个字母变成大写,其他字母变小写。对于 8 位字节编码需要根据本地环境。
# 语法：str.capitalize()
#     Name = 'chen'
#     A = Name.capitalize()
#     print (A)
#
# Python center()
# Python center() 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格
# 语法：str.center(width[, fillchar])
#     A = Name.center(20,'#')
#     print (A)
#
# Python count()
# Python count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
# 语法：str.count(sub, start= 0,end=len(string))
#     Name = 'aabbbbb2222ddddsaaadffffsss'
#     A = Name.count('a',0,10)
#     print (A)
#
# Python encode()
# Python encode() 方法以 encoding 指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。
# 语法：str.encode(encoding='UTF-8',errors='strict')
#     Name= "陈金彭"
#     A = Name.encode('gbk')
#     print(A)
#
# Python endswith()
# 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。可选参数"start"与"end"为检索字符串的开始与结束位置。
# 语法：str.endswith(suffix[, start[, end]])
#     A = Name.endswith('e',0,3)
#     print (A)
#
# Python expandtabs()
# Python expandtabs() 方法把字符串中的 tab 符号('\t')转为空格，默认的空格数 tabsize 是 8。
# 语法：str.expandtabs(tabsize=8)
# Name = 'ch\ten'
#     A = Name.expandtabs(tabsize=100)
#     print (A)
#
# Python find()
# Python find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
# 语法：str.find(str, beg=0, end=len(string))
#     Name = 'abcaaaahhhhbbbbcccc'
#     A = Name.find('c',10,16)
#     print (A)
#
# python format()字符串格式化
#     Name = "陈金彭"
#     Age = 17
#     print ('My Name is {0},Age is {1}'.format(Name,Age))
#
# Python index()
# Python index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
# 语法：str.index(str, beg=0, end=len(string))
#     A = Name.index('g')
#     print (A)
#
# Python isalnum()
# Python isalnum() 方法检测字符串是否由字母和数字组成。
# 语法：str.isa1num()
#     A = Name.isalnum()
#     print (A)
#
# Python isalpha()
# Python isalpha() 方法检测字符串是否只由字母组成。
# 语法：str.isalpha()
#     Name = '111'
#     A = Name.isalpha()
#     print (A)
#
# Python isdigit()
# Python isdigit() 方法检测字符串是否只由数字组成。
# 语法：str.isdigit()
#     A = Name.isdigit()
#     print (A)
#
# Python islower()
# Python islower() 方法检测字符串是否由小写字母组成。
# 语法：str.islower()
#     A = Name.islower()
#     print (A)
#
# Python isspace()
# Python isspace() 方法检测字符串是否只由空格组成。
# 语法：str.isspace()
#     Name = '   '
#     A = Name.isspace()
#     print (A)
#
# Python istitle()
# Python istitle() 方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。
# 语法：str.istitle()
#     Name = 'Aaad Aa'
#     A = Name.istitle()
#     print (A)
#
# Python isupper()
# Python isupper() 方法检测字符串中所有的字母是否都为大写。
# 语法：str.isupper()
#     Name='CHEN'
#     A = Name.isupper()
#     print (A)
#
# Python isdecimal()
# Python isdecimal() 方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。注意:定义一个十进制字符串，只需要在字符串前添加 'u' 前缀即可。
# 语法：str.isdecimal()
#     Name = '123'
#     A=Name.isdecimal()
#     print (A)
#
# Python isnumeric()
# Python isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。注：定义一个字符串为Unicode，只需要在字符串前添加 'u' 前缀即可，具体可以查看本章节例子
# 语法：str.isnumeric()
#     Name = '123'
#     A=Name.isnumeric()
#     print (A)
#
# Python join()
# Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
# 语法：str.join(sequence)
#     A = '陈'
#     B = '金彭'
#     print(''.join([A,B]))
#
# Python ljust()
# Python ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串
# 语法：str.ljust(width[, fillchar])
#     A = Name.ljust(5,'#')
#     print (A)
#
# Python lower()
# Python lower() 方法转换字符串中所有大写字符为小写。
# 语法：str.lower()
#     Name='CHEN'
#     A = Name.lower()
#     print (A)
#
# Python lstrip()
# Python lstrip() 方法用于截掉字符串左边的空格或指定字符。
# 语法;str.lstrip([chars])
#     Name='   chenjin  peng  '
#     A = Name.lstrip()
#     print (A)
#
# ###maketrans以及translate方法解释：
# Python maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。注：两个字符串的长度必须相同，为一一对应的关系。
# Python translate() 方法根据参数table给出的表(包含 256 个字符)转换字符串的字符, 要过滤掉的字符放到 del 参数中。
#     A='abcde'
#     B='12345'
#     AA = str.maketrans(A,B)
#     CC='my name is chen...abe'
#     print(CC.translate(AA))
#
# Python upper()
# Python upper() 将字符串转换为全大写（字符串：ASCII字符）
# 语法：str.upper()
#     A = Name.upper()
#     print (A)
#
# partition()
# partition() 方法用来根据指定的分隔符将字符串进行分割。如果字符串包含指定的分隔符，则返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。partition() 方法是在2.5版中新增的
# 语法：str.partition(str)
#     A=Name.partition('e')
#     print(type(A))
#
# Python replace()
# Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
# 语法：str.replace(old, new[, max])
#     A=Name.replace('h','a')
#     print (A)
#
# Python rfind()
# Python rfind() 返回字符串最后一次出现的位置，如果没有匹配项则返回-1。
# 语法str.rfind(str, beg=0 end=len(string))
#     A=Name.rfind('n',0,4)
#     print(A)
#
# Python rindex()
# Python rindex() 返回子字符串 str 在字符串中最后出现的位置，如果没有匹配的字符串会报异常，你可以指定可选参数[beg:end]设置查找的区间。
# 语法：str.rindex(str, beg=0 end=len(string))
#     A=Name.rindex('c')
#     print (A)
#
# Python rjust()
# Python rjust() 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串
# 语法：str.rjust(width[, fillchar])
#     A=Name.rjust(5,'#')
#     print (A)
#
# Python.rpartition()
# Python.rpartition() 分割字符串，（从右往左）返回元组
# 语法：str.rpartition(str)
#     A=Name.rpartition('h')
#     print (A)
#
# Python splitlines()
# Python splitlines() 按照行分隔，返回一个包含各行作为元素的列表，如果 num 指定则仅切片 num 个行.
# 语法：str.splitlines( num=string.count('\n'))
#     Name = 'chen jin peng\nqiu lu nan'
#     print (Name.splitlines())
#
# Python startswith()
# Python startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 start 和 end 指定值，则在指定范围内检查。
# 语法：str.startswith(str, beg=0,end=len(string));
#     A=Name.startswith('c')
#     print(A)
#
# Python strip()
# Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
# 语法：str.strip([chars]);
#     Name='        chen\n  '
#     A=Name.strip()
#     print (A)
#
# Python swapcase()
# Python swapcase() 方法用于对字符串的大小写字母进行转换。
# 语法：str.swapcase();
#     Name = 'CHEN'
#     A=Name.swapcase()
#     print(A)
#
# Python title()
# Python title() 方法返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())。
# 语法str.title();
#     Name='chen_jinpeng'
#     A=Name.title()
#     print(A)
#
# Python upper()
# Python upper() 方法将字符串中的小写字母转为大写字母。
# 语法:str.upper()
#     A=Name.upper()
#     print(A)
#
# Python zfill()
# Python zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。
# 语法：str.zfill(width)
#     print (Name.zfill(80))
#     print(Name.zfill(79))

# ##########################列表##########################
# Name = ['chen','alex','wu']
# append()
# append() 方法用于在列表末尾添加新的对象。
# 语法：list.append(obj)
# Name.append('65年哥')
# print (Name)
#
# clear()
# clear()方法用户删除所有列表中的元素
# 语法:list.clear()
# Name.clear()
# print (Name)
#
# copy()方法
# copy()方法用户copy列表中的元素，【浅拷贝】
# 语法：list.copy()
# Name2=Name.copy()
# print(Name2)
#
# count() 方法
# count() 方法用于统计某个元素在列表中出现的次数。
# 语法：list.count(obj)
# A=Name.count('alex')
# print(A)
#
# extend()
# extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
# 语法：list.extend(seq)
# Name2=['猴子','瘸子']
# Name.extend(Name2)
# print(Name)
#
# index()
# index() 函数用于从列表中找出某个值第一个匹配项的索引位置。
# 语法：list.index(obj)
# A=Name.index('wu')
# print(A)
#
# insert()
# insert() 函数用于将指定对象插入列表。
# 语法:list.insert(index, obj)
# Name.insert(1,'65武姐姐')
# print(Name)
#
# pop()
# pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
# 语法list.pop(obj=list[-1])
# A=Name.pop()
# print(A,Name)
#
# remove()
# remove() 函数用于移除列表中某个值的第一个匹配项。
# 语法:list.remove(obj)
# Name.remove('alex')
# print(Name)
#
# reverse()
# reverse() 函数用于反向列表中元素。
# 语法:list.reverse()
# Name.reverse()
# print(Name)
#
# sort()
# sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
# 语法:list.sort([func])
# Name=['1','2','A','B','a','b','一','二','!','%']
# Name.sort()
# print(Name)

##########################元组##########################
# Name=('chen','wu','alex','chen')
# count()
# count() 方法用于统计某个元素在元组中出现的次数。
# 语法：tuple.count(obj)
# A=Name.count('chen')
# print(A)
#
# index()
# index() 函数用于从列表中找出某个值第一个匹配项的索引位置。
# 语法：tuple.index(obj)
# A=Name.index('alex')
# print(A)


##########################字典##########################

# Dic={'k1':'value1','k2':'value2'}
#
# clear()
# clear() 函数用于删除字典内所有元素。
# 语法：dict.clear()
# Dic.clear()
# print(Dic)
#
# dict.copy()
# Python 字典(Dictionary) copy() 函数返回一个字典的浅复制。
# 何为浅复制：(浅拷贝 在副本中替换值的时候 原字典不受影响， 如果修改或者删除了深层（非第一层）的值 原始的字典也会改变，为了避免这种情况，就使用深拷贝)
# 语法：dict.copy()
# Dic={'k1':{'value1':['aaaa',123]},'k2':'value2'}
# Dic2=Dic.copy()
# # print(Dic2)
# Dic2['k1']['value1'][1]=1234
# Dic2['k1']['value1'].remove('aaaa')
# print(Dic2)
# print(Dic)
# 另一案例
# a={'k1':'v1','k2':[11,22,33]}
# print(id(a),a)
# print(id(a['k2']),a['k2'])
# b=dict.copy(a)
# print(id(b),b)
# print(id(b['k2']),b['k2'])
# print(id(a['k1']),a['k1'])
# print(id(b['k1']),b['k1'])
# print(a.keys(),id(a.keys()))
# print(b.keys(),id(b.keys()))
#
# fromkeys()
# Python 字典(Dictionary) fromkeys() 函数用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值。
# 语法：dict.fromkeys(seq[, value]))
# Seq=['name','age','sex']
# Dic=dict.fromkeys(Seq)
# print(Dic)
# Dic=dict.fromkeys(Seq,10)
# print(Dic)
#
# get()
# Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值None。
# 语法：dict.get(key, default=None)
# A=Dic.get('k1')
# print(A)
#
# items()
# Python 字典(Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组。
# 语法:dict.items()
# A=Dic.items()
# print(A)
#
# keys()
# Python 字典(Dictionary) keys() 函数以列表返回一个字典所有的键。
# 语法:dict.keys()
# A=Dic.keys()
# print(A)
#
# pop()
# pop() 函数用于移除字典中指定的keys，并将其value删除，并且返回该元素的值。
# 语法:dict.pop(obj)
# A=Dic.pop('k1')
# print(A,Dic)
#
# popitem()
# dict.popitem()方法删除字典中随机的键，值
# 语法：dict.popitem()
# A=Dic.popitem()
# print(A,Dic)
#
# setdefault()
# Python 字典(Dictionary) setdefault() 函数和get()方法类似,如果键存在，打印value，如果键不存在于字典中，将会添加键并将值设为默认值。
# 语法:dict.setdefault(key, default=None)
# A=Dic.setdefault('k3','noexit')
# print(A,Dic)
#
#  update()
# Python 字典(Dictionary) update() 函数把字典dict2的键/值对更新到dict里。
# 语法:dict.update(dict2)
# A={'name','chen'}
# B={'age','18'}
# A.update(B)
# print(A)
#
# values()
# Python 字典(Dictionary) values() 函数以列表返回字典中的所有值。
# 语法:dict.values()
# A=Dic.values()
# print(A)
#
# dict.__contains__() #查找字符串是否存在字典中的keys，返回True或者False
# Search='k1'
# print(Dic)
# A=Dic.__contains__(Search)
# print(A)

