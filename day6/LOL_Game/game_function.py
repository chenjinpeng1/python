#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import os,sys,time,random
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE)
from LOL_Game import Game_Life
from PAONIU import paoniu
Res = True
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
    Count = 0
    def __init__(self,name,Life_Val,damage,skills,D_name,D_Life_Val,D_skills,D_damage):
        super(Attack,self).__init__(name,Life_Val,damage,skills)
        self.D_name = D_name
        self.D_Life_Val = D_Life_Val
        self.D_skills = D_skills
        self.D_damage = D_damage


    def attack(self):
        """
        选择性攻击
        """
        global Res
        Res = True
        A=[]
        for i in (self.skills):
            A.append(i)
        A.append(['普通攻击',self.damage])
        while Res:
            for index,i in enumerate(A,1):print(index,i)
            Option = input('请选择释放的技能：')
            Judge_res= Game_Life.Judge_Options(Option, A)
            if Judge_res:
                if Option == '5':
                    ShangHai = self.damage
                    GongJi = '普通攻击'
                else:
                    ShangHai = self.skills[int(Option)-1][1]
                    GongJi = self.skills[int(Option)-1][0]
                self.D_Life_Val-=int(ShangHai)
                print('[%s] 向 [%s] 释放技能 [%s] , 扣除[%s]生命,[%s] 剩余生命 [%s]\n' %(self.name,self.D_name,GongJi,ShangHai,self.D_name,self.D_Life_Val))
                if self.D_Life_Val <= 0:
                    print('[%s] game over！！'%self.D_name)
                    Res = False
                    # break
                else:self.Auto()
            else:continue


    def Auto(self):
        '''
        自动攻击函数
        '''
        global Res
        while Res:
            A=random.randrange(0,5)
            if A == 4:
                ShangHai = self.D_damage
                GongJi = '普通攻击'
            else:
                ShangHai = self.D_skills[A][1]
                GongJi = self.D_skills[A][0]
            self.Life_Val-=int(ShangHai)
            Attack.Count+=1
            print('[%s] 向 [%s] 释放技能 [%s] , 扣除[%s]生命,[%s] 剩余生命 [%s]\n' %(self.D_name,self.name,GongJi,ShangHai,self.name,self.Life_Val))
            print('''
 -------------------- 第%s回合结束 --------------------
            '''%Attack.Count)
            if self.Life_Val <= 0:
                print('[%s] game over！！'%self.D_name)
                Res = False
                break
            else:
                self.attack()

    def Print_xiaoguo(self,p):
        '''
        打印延迟函数
        '''
        for i in p:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)

    def HoneWork(self):
        """
        写作业函数
        """
        f = open('index.py','r',encoding='utf-8')#LOL_Game/Game_Life.py
        for i in f.readlines():
            self.Print_xiaoguo(i)
        p=('写完啦~~~~~泡妞去咯 哈哈哈哈哈哈哈！\n')
        self.Print_xiaoguo(p)
        self.paoniu()
    def paoniu(self):
        '''
        泡妞函数
        '''
        name = input('请输入你的名字：')
        info = paoniu.MAN(name)
        info[name] = info['alex']
        info2 = paoniu.Girl()
        Options = list(info2.keys())
        for index,i in enumerate(Options):
            print(index,i)
        Option = input('请输入你想泡的妞：')
        aa=paoniu.TanLa(info,info2,Options[int(Option)],name)
        while True:
            try:
                a,b=aa.__next__()
                print1=('[%s]:%s\n'%(name,a))
                print2=('[%s]:%s\n'%(Options[int(Option)],b))
                self.Print_xiaoguo(print1)
                self.Print_xiaoguo(print2)
            except StopIteration:
                break

# --------------------------------------------------------------------------------- #
