#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
print(sys.path)
from LOL_Game import Game_Life

if __name__ == '__main__':
    Game_Life.Game_index()
