#python 3.5环境,解释器在linux需要改变
#商城购物，阅读手册查询readme文件
#作者：S12-陈金彭
import sys
import os
DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(DIR)
from backend.db import sql_api
def home():
    print('welcome to home page!')
    q_data = sql_api.select("root",'123')
    print(q_data)
def movie():
    print('welcome to movie page!')
def tv():
    print('welcome to tv page!')