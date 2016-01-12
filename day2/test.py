# dic = {}
# Nul = [11,22,33,44,55,66,77,88,99]
# for i in  Nul:
#     if i > 66:
#         dic.setdefault(i,'大于66')
#     else:
#          dic.setdefault(i,'小于66')
# print (dic)
# for i,val in dic.items():
#     print (i,val)

# 作业1：购物车
# result = 'dengyu' if 1==1 else 'budengyu'
# print (result)
# print (int('f',base=16)) #将任意类型的禁制按照指定的禁制转换为10禁制

# aa={'a':'b','b':'c'}
# print(type(aa.keys()))

dic = {}
Nul = [11,22,33,44,55,66,77,88,99]
for i in Nul:
    if i > 66:
        if 'k1' in dic.keys():
            dic['k1'].append(i)
        else:
            dic['k1']=[i,]
    if i <= 66:
        if 'k2' in dic.keys():
            dic['k2'].append(i)
        else:
            dic['k2']=[i,]
print(dic)

































































