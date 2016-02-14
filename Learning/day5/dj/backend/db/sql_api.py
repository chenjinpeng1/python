#python 3.5环境,解释器在linux需要改变
#商城购物，阅读手册查询readme文件
#作者：S12-陈金彭
import os
import sys
DIR=(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(DIR)
from config.settings import config
def select():
    if config()['user'] == 'root' and config()['password'] == '123 '

