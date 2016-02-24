#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
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
        # self.damage_distance = damage_distance # 攻击距离
        self.skills = skills  # 技能
'''
攻击类
'''
class Attack(Hero_Pool):
    def __init__(self,name,D_name,Life_Val,D_Life_Val,damage,D_damage,skills,D_skills):
        super(Attack,self).__init__(name,Life_Val,damage,skills)
        self.D_name = D_name
        self.D_Life_Val = D_Life_Val
        self.D_damage = D_damage
        self.D_skills = D_skills
    def attack(self):
        print('[%s] 像 [%s] 做出攻击 [%s] , 扣除[%s]生命,[%s]剩余生命[%s]' %(self.name,self.D_name,self.skills,self.D_damage,self.D_name,int(self.D_Life_Val)-self.damage))

# --------------------------------------------------------------------------------- #

# S1=Attack('AnNi','盖伦','500','1000','80','90','碎裂之火','审判之剑')
# S1.attack()
