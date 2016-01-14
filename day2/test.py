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

# dic = {}
# Nul = [11,22,33,44,55,66,77,88,99]
# for i in Nul:
#     if i > 66:
#         if 'k1' in dic.keys():
#             dic['k1'].append(i)
#         else:
#             dic['k1']=[i,]
#     if i <= 66:
#         if 'k2' in dic.keys():
#             dic['k2'].append(i)
#         else:
#             dic['k2']=[i,]
# print(dic)
import login
Shopping={
    'Macbook Air':[10,7999],
    'Iphone 6s  ':[10,6543],
    '冰箱       ':[10,3999],
          }
# aa=list(Shopping.items())
# a=''
# for k,val in enumerate(aa):
#    a+=''.join([str(k),''.center(20,' '),str(val[0]),''.center(30,' '),str(val[1][0]),''.center(30,' '),str(val[1][1]),'\n'])
# print(a)

print(type(Shopping['冰箱       '][1]))
# bb=list(Shopping.keys())
# print(bb)
# print(Shopping[bb[0]][1])
# a=''
# for i,val in enumerate(bb):
#     print(i,val,)
#     a += ''.join([str(i),val,str(Shopping[val][1]),'\n'])
# print(a)
# A=[0,1,2,3,4,5]
# A.remove(A[1])
# print(A)
a=2
b=1
a-=b
print(a)


























































