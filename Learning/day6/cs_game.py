#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
class Role(object):
    ac = None
    def __init__(self,name,role,weapon,life_value):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
    def buy_weapon(self,weapon):
        print("%s is buying [%s]"%(self.name,weapon))
        self.weapon = weapon
p1 = Role('JinPeng','Polic','B10',90)
p2 = Role('LuNan','tufei','B11',100)
p1.buy_weapon('AK47')
p2.buy_weapon('B51')
p1.ac = 'China '
print("p1:",p1.weapon,p1.ac)
print('p2:',p2.weapon,p2.ac)

