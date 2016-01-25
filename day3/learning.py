# import collections
# # aa = collections.OrderedDict()
# # aa={}
# aa = collections.defaultdict(list)
# aa[1].append(1)
# print(aa)
# c=[1,1,1,2,2,3,2,1,4,5,6]
#
# c = collections.Counter(c)
# print(c)
# li = [13, 22, 6, 99, 11]
# a=0
# for m in range(len(li)):
#     for n in range(m, len(li)):
#         if li[m]> li[n]:
#             temp = li[n]
#             li[n] = li[m]
#             li[m] = temp
# print (li)

# ------------------------------------------集合------------------------------------------#
# old_dict = {
#     "#1":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
#     "#2":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
#     "#3":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
# }
#
# # cmdb 新汇报的数据
# new_dict = {
#     "#1":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 800 },
#     "#3":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
#     "#4":{ 'hostname':'c2', 'cpu_count': 2, 'mem_capicity': 80 },
# }
# old = set(old_dict.keys())
# new = set(new_dict.keys())
# print(old)
#
# print(new)
# update_set = old.intersection(new)  #取交集   1 3
# delete_set = old.difference(new)   #取差集 2
# add_set = new.difference(old)    #取差集4
# # print(update_set) # 1 3
# # print(delete_set) # 2
# # print(add_set) # 4
# # #
# # old.intersection_update(new)   #取交集并更新
# # print(old)
# print(old.symmetric_difference(new)) # 取交叉集
#实例2：
# a = set([1,2,3])
# b = set([1,3,4])
# a.intersection_update(b)
# # print(a)
# c = b.difference(a)
# print(c)
# a.update(c)
# print(a)

# ------------------------------------------conllections计数器------------------------------------------#
# import collections
# obj = collections.Counter('sdfjkqwertcasdfgwertzxv')
# print(obj)
# for i in obj.items():
#     print(i)
# ret = obj.most_common(3) #取前三个元素
# print(ret)
# for i in obj.elements():  #打印未经过处理的全部元素，
#     print(i)
# for i in obj.keys():  #打印经过Counter处理的数据
#     print(i)
# ------------------------------------------conllections有序字典------------------------------------------#
import collections
# a = collections.OrderedDict()
# a[1]=1
# a[2]=2
# a[3]=3
# # a.clear()
# # print(a)
# a[1]=2
# print(a)
# ------------------------------------------conllections默认字典------------------------------------------#
# aa = collections.defaultdict(list)
# aa[1].append(1)
# print(aa)
# ------------------------------------------深浅copy------------------------------------------#
# Dic={'k1':{'value1':['aaaa',123]},'k2':'value2'}
# Dic2=Dic.copy()
# print(Dic)
# print(Dic2)
# Dic2['k2']='aaaaa'
# print(Dic2)
# print(Dic)
# Dic2['k2']='bbbbbb'
# print(Dic2)
# print(Dic)
# Dic2['k1']['value1'][1]=1234
# print(Dic2)
# print(Dic)
# Dic2['k1']['value1'].remove('aaaa')
# print(Dic2)
# print(Dic)
# Dic2['k1']['value1'].append(111111)
# print(Dic2)
# print(Dic)
# #另一案例
# a={'k1':'v1','k2':[11,22,33]}
# print(id(a),a)
# b=dict.copy(a)
# print(id(b),b)
# c=a
# print(id(a['k2']),a['k2'])
# print(id(b['k2']),b['k2'])
# print(id(a['k1']),a['k1'])
# print(id(b['k1']),b['k1'])
# print(a.keys(),id(a.keys()))
# print(b.keys(),id(b.keys()))
# import copy
# a='123'
# b=copy.copy(a)
# print(id(a))
# print(id(b))
# b=456
# print(a)
# print(b)