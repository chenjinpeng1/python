#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Role(object):
    # members  = 0
    def __init__(self,name,role,weapon,life_value):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_val = life_value
        # Role.members +=1
    def buy_weapon(self,weapon):

        print("%s is buying [%s]" %(self.name,weapon))
        self.weapon = weapon
        # print(self)
#role 的实例
#把一个抽象的类变成一个具体的对象的过程 叫实例化
p1= Role("SanJiang",'Police',"B10",90)
t1= Role("ChunYun",'Terrorist',"B11",100)
# t2= Role("T2",'Terrorist',"B17",100)
# t3= Role("T3",'Terrorist',"B19",100)
p1.buy_weapon("AK47") #Role.buy_weapon(p1,"AK47")
t1.buy_weapon("B51")

# p1.ac = "China Brand"
# t1.ac = "US Brand"
# Role.ac = "Janpanese Brand"
print("P1:",p1.weapon)
print("T1:",t1.weapon)
# print("T2:",t2.ac,t2.weapon)
# print("T3:",t3.ac,t3.weapon)
# print(Role.buy_weapon)
