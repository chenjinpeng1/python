#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import random
class LOL(object):
    def __init__(self,user,age,sex):
        self.user = user
        self.age = age
        self.sex = sex
'''
定义英雄的默认属性
'''
class Hero_Pool(object):
    def __init__(self,name,Life_Val,damage,skills):
        self.name = name  # 英雄名字
        self.Life_Val = Life_Val    # 生命值
        self.damage = damage   #攻击力
        self.skills = skills  # 技能
'''
攻击类
'''
class Attack(Hero_Pool):
    def __init__(self,name,Life_Val,damage,skills,D_name,D_Life_Val,D_skills,D_damage):
        super(Attack,self).__init__(name,Life_Val,damage,skills)
        self.D_name = D_name
        self.D_Life_Val = D_Life_Val
        self.D_skills = D_skills
        self.D_damage = D_damage
    def attack(self):
        Res = True
        while Res:
            A=[]
            for i in (self.skills):
                A.append(i)
            A.append(['普通攻击',self.damage])
            for index,i in enumerate(A,1):print(index,i)
            Option = input('请选择释放的技能：')
            if Option == '5':
                ShangHai = self.damage
                GongJi = '普通攻击'
            else:
                ShangHai = self.skills[int(Option)-1][1]
                GongJi = self.skills[int(Option)-1][0]
            self.D_Life_Val-=int(ShangHai)
            print('[%s] 像 [%s] 释放技能 [%s] , 扣除[%s]生命,[%s]剩余生命[%s]' %(self.name,self.D_name,GongJi,ShangHai,self.D_name,self.D_Life_Val))
            if self.D_Life_Val <= 0:
                print('[%s] game over！！'%self.D_name)
                Res = False
                # break
            else:self.Auto()
    def Auto(self):
        Res2 = True
        while Res2:
            A=random.randrange(0,5)
            if A == 4:
                ShangHai = self.D_damage
                GongJi = '普通攻击'
            else:
                ShangHai = self.D_skills[A][1]
                GongJi = self.D_skills[A][0]
            self.Life_Val-=int(ShangHai)
            print('[%s] 像 [%s] 释放技能 [%s] , 扣除[%s]生命,[%s]剩余生命[%s]' %(self.D_name,self.name,GongJi,ShangHai,self.name,self.Life_Val))
            if self.Life_Val <= 0:
                print('[%s] game over！！'%self.D_name)
                break
            else:
                self.attack()
# --------------------------------------------------------------------------------- #
