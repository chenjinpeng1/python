#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import pickle,collections,random,game_function
# from game_function import Attack
print(('=*'*20).rjust(80))
print('|'.rjust(41),'LOL Game Start'.rjust(25),'|'.rjust(12))
print(('=*'*20).rjust(80))
# Hero_attribute=collections.OrderedDict()
# Hero_attribute['AnNi'] = ['AnNi',2000,80,[['碎裂之火','80'],['焚烧',70],['熔岩护盾',20],['提伯斯之怒',175]]]
# Hero_attribute['诡术妖姬'] = ['诡术妖姬',1500,60,[['恶意魔印','55'],['魔影迷踪',85],['幻影锁链',40],['故技重施',200]]]
# Hero_attribute['末日使者'] = ['末日使者',1800,65,[['恐惧','55'],['吸血',85],['沉默',60],['乌鸦来袭',200]]]
# Hero_attribute['小鱼人'] = ['小鱼人',1900,80,[['淘气打击','83'],['攻击附加',30],['古灵精怪',100],['巨鲨强袭',200]]]
# Hero_attribute['盖伦'] = ['盖伦',3000,85,[['沉默','85'],['护甲守卫',10],['审判之转',120],['审判之剑',350]]]
# Hero_attribute['剑圣'] = ['剑圣',2300,90,[['阿尔法突袭','100'],['冥想',85],['无极剑道',20],['高原血统',400]]]
# Hero_attribute['寒冰射手'] = ['寒冰射手',1500,150,[['冰霜射击','99'],['万箭齐发',100],['鹰击长空',30],['魔法之箭',250]]]
# Hero_attribute['伊泽瑞尔'] = ['伊泽瑞尔',2000,120,[['秘术射击','100'],['精华跃动',90],['奥术跃迁',90],['精准弹幕',300]]]
f=open('info.txt','rb')
# f.write(pickle.dumps(Hero_attribute))
Hero_attribute=pickle.loads(f.read())
Menu=['选择英雄','退出']
for index,i in enumerate(Menu,1):print('[%s]     %s'.rjust(61)%(index,i))
Option = input('请输入操作')
if Option == '1':
    A=[]
    for index,i in enumerate(Hero_attribute,1):
        print(index,i)
        A.append(i)
    # print('%s'.rjust(28) %(''.join(A)))
    Hero_1 = input('选择参战的第一个英雄：')
    JiNeng=[]
    for i in Hero_attribute[A[int(Hero_1)-1]][3]:
        JiNeng.append(i[0])
    print('[%s] 的技能为%s'%(A[int(Hero_1)-1],JiNeng))
    Hero_2 = input('选择参战的第二个英雄：')
    JiNeng=[]
    for i in Hero_attribute[A[int(Hero_2)-1]][3]:
        JiNeng.append(i[0])
    print('[%s] 的技能为%s'%(A[int(Hero_2)-1],JiNeng))
    print('战斗开始')
    res = True
    # X1=game_function.Attack('AnNi','盖伦','500','1000',80,90,'碎裂之火','审判之剑')
    # game_function.X1.acctack()

    while res:
        S_name = A[int(Hero_1)-1]
        D_name = A[int(Hero_2)-1]
        S_Life_Val = Hero_attribute[S_name][1]
        D_Life_Val = Hero_attribute[D_name][1]
        S_damage = Hero_attribute[S_name][2]
        D_damage = Hero_attribute[D_name][2]
        A=random.randrange(1,6)

    #     X1=Attack('AnNi','盖伦','500','1000',80,90,'碎裂之火','审判之剑')
        X1=('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'%(A[int(Hero_1)-1],A[int(Hero_2)-1],Hero_attribute[]))
    #     X1.attack()
    #     res = False



