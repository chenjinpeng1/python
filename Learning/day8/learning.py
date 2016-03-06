#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
# try:
#     # import aa
#     a = [11,22]
#     # print(a[3])
#     if bb == 3:
#         print("aaa")
#     bb=input(">>>:")
#     aa = int(bb)
# # except IndexError as e:
# #     print("indexError")
# #     print(e)
#
# except ImportError as e:
#     print('importError')
#     print(e)
#
# except AttributeError as e:
#     print("AttributeError")
#     print(e)
# except IOError as e:
#     print('IOError')
#     print(e)
class ChenException(Exception):
    def __init__(self,msg):
        self.message = msg
    def __str__(self):
        return self.message
# a=1
try:
    raise ChenException("我的异常")
except Exception as e:
    print(e)
ChenException("我的异常")
