#python 3.5环境,解释器在linux需要改变
#商城购物，阅读手册查询readme文件
#作者：S12-陈金彭
import sys
import os
DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(DIR)
from config import settings
def db_auth(user,passwd):
    if settings.DATABASE['user'] == user and settings.DATABASE['password'] == passwd:
        print('db auth passed!')
        return True
    else:print('db login error.....')
def select(user,passwd):
    if db_auth(user,passwd):
            user_info = {
                "001":['alex',22,'enginner'],
                "002":['longGe',43,'chef'],
                "003":['xiaoYun',23,'13baoan'],
            }
            return user_info
