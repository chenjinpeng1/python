# import sys
# a = "1"
# print (sys.argv)
# a = (1,2,3,{'key1':'val1'})
# a[3]['key1'] = 2222
# # print (a[3]['key1'])
# print (a)
#type
#dir
# divmod(10,3) 取结果和余数
a = 'aaab'
# b = a.__contains__(a) 判断a是否在变量a里 等价于 'aa' in a
# print (b)
#a.__getattribute__() 反射会用
# name.casefold() 首字母大小变小写
#a.capitalize()首字母小写变大写
# a.center(20,*)#居中
# a.count('a',0,2)查找出现的次数
# a.encode('gbk') 将utf-8转换为gbk
# a.endswith('a',0,3)判断字符串是否已a结尾 0 ，3 从第零个字符到第三个字符
# a.expandtabs()将变量a里的所有tab转换为空格
# a.find(b) 在变量a种查找字符可以设置起始位置与结束位置，返回其索引值 与a.index等同 但是index如果找不到则直接报错，find会返回-1
# a.format('aa','bb')字符串拼接还是(替换) a = 'alex {0} as {1}'
# a.isalnum()判断是否是字母或者数字
# ''.join(a)
# a.ljust() 注意是L 不是1
# a.maketrans()
# a.partition('aa') 分割 按照aa分割
# a.replace('a','p'，1) 替换a 为p 后面的1表示为制转换第一个 可以为2.3.4 等
# a.rfind()从又开始找
# a.split()分割字符串为列表
# a.swapcase()大小写转换
# a.title()字符串首字母大写
a='-12+1'
try:
    if (type(float(a))) is float:
        print('aaaaa')
except Exception:
    pass

