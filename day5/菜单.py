#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import os,sys,random
DIR=os.path.dirname(os.path.abspath(__file__))
sys.path.append(DIR)
from Shop import shop
from Card import main
print('#-------使用前请先注册信用卡、购物商城用户   |    信用卡利息需更改完系统时间，再次查看账户信息-------#')
mains=['登陆购物商城','登陆信用卡']
for index,i in enumerate(mains,1):
    print(index,i)
Option=input('请选择你的操作：')
if Option=='1':
    shop.shop()
if Option=='2':
    main.main()