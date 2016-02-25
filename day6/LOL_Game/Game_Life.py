#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import os,sys,collections
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE)
from LOL_Game import game_function

'''
判断用户输入是否正确
'''
def Judge_Options(str,des):
    if str.isdigit() is True:
        if des != '0':
            if int(str) <= len(des) and  int(str) != 0:
                return True
            else:
                print('输入正确的序列')
                return False
    else:
        print('输入正确的选项!')
        return False
# if __name__ == '__main__':
def Game_index():
    '''
    游戏开始调用页面
    '''

    RES = True
    while RES:
        print(('=*'*20).rjust(80))
        print('|'.rjust(41),'LOL Game Start'.rjust(25),'|'.rjust(12))
        print(('=*'*20).rjust(80))
        Hero_attribute=collections.OrderedDict()
        Hero_attribute['AnNi'] = ['AnNi',2000,80,[['碎裂之火','80'],['焚烧',70],['熔岩护盾',20],['提伯斯之怒',175]]]
        Hero_attribute['诡术妖姬'] = ['诡术妖姬',1500,60,[['恶意魔印','55'],['魔影迷踪',85],['幻影锁链',40],['故技重施',200]]]
        Hero_attribute['末日使者'] = ['末日使者',1800,65,[['恐惧','55'],['吸血',85],['沉默',60],['乌鸦来袭',200]]]
        Hero_attribute['小鱼人'] = ['小鱼人',1900,80,[['淘气打击','83'],['攻击附加',30],['古灵精怪',100],['巨鲨强袭',200]]]
        Hero_attribute['盖伦'] = ['盖伦',3000,85,[['沉默','85'],['护甲守卫',10],['审判之转',120],['审判之剑',350]]]
        Hero_attribute['剑圣'] = ['剑圣',2300,90,[['阿尔法突袭','100'],['冥想',85],['无极剑道',20],['高原血统',400]]]
        Hero_attribute['寒冰射手'] = ['寒冰射手',1500,150,[['冰霜射击','99'],['万箭齐发',100],['鹰击长空',30],['魔法之箭',250]]]
        Hero_attribute['伊泽瑞尔'] = ['伊泽瑞尔',2000,120,[['秘术射击','100'],['精华跃动',90],['奥术跃迁',90],['精准弹幕',300]]]
        Hero_attribute['吴三江'] = ['吴三江',2000,0,[['哥，我错了 别打我','0'],['哥，我错了 别打我',0],['哥，我错了 别打我',0],['怒气冲天',1]]]

        Menu=['选择英雄','退出']
        for index,i in enumerate(Menu,1):print('[%s]     %s'.rjust(61)%(index,i))
        Option = input('请输入操作')
        Judge_res=Judge_Options(Option,Menu)
        if Judge_res:
            if Option == '1':
                while Judge_res:
                    # 将英雄添加到列表
                    A=[]
                    for index,i in enumerate(Hero_attribute,1):
                        print(index,i)
                        A.append(i)
                    Hero_1 = input('选择参战的第一个英雄(q退出)：')
                    if Hero_1 != 'q':
                        # 进行判断输入是否有误
                        Judge_res2=Judge_Options(Hero_1,A)
                        if Judge_res2:
                            # 获取技能信息
                            JiNeng=[]
                            for i in Hero_attribute[A[int(Hero_1)-1]][3]:
                                JiNeng.append(i[0])
                            print('[%s] 的技能为%s'%(A[int(Hero_1)-1],JiNeng))
                            Hero_2 = input('选择参战的第二个英雄：')
                            Judge_res3=Judge_Options(Hero_2,A)
                            if Judge_res3:
                                JiNeng2=[]
                                for i in Hero_attribute[A[int(Hero_2)-1]][3]:
                                    JiNeng2.append(i[0])
                                print('[%s] 的技能为%s'%(A[int(Hero_2)-1],JiNeng2))
                                print('战斗开始')
                                S_name = A[int(Hero_1)-1]  #原英雄名
                                D_name = A[int(Hero_2)-1] # 目标英雄名
                                S_Life_Val = Hero_attribute[S_name][1] #原英雄生命值
                                D_Life_Val = Hero_attribute[D_name][1] #目标英雄生命值
                                S_damage = Hero_attribute[S_name][2] #原初始攻击力
                                D_damage = Hero_attribute[D_name][2] #目标初始攻击力
                                X1= game_function.Attack(S_name, S_Life_Val, S_damage, Hero_attribute[S_name][3], D_name, D_Life_Val, Hero_attribute[D_name][3], D_damage)
                                X1.attack()
                                p=('----别玩了，在不写作业又该挨大王骂你了.....\n')
                                X1.Print_xiaoguo(p)
                                Options_Main = ['算了，真没意思，不完了 写作业去','我还要继续玩，游戏人生']
                                RES2=True
                                while RES2:
                                    for index,i in enumerate(Options_Main,1):
                                        print(index,i)
                                    Next_option =input('请选择：')
                                    Judge_res4=Judge_Options(Next_option,Options_Main)
                                    if Judge_res:
                                        if Next_option == '1':
                                            X1.HoneWork()
                                            Judge_res=False
                                            RES = False
                                            break
                                        if Next_option == '2':
                                            Judge_res=False
                                            break
                                    else:continue
                        else:
                            continue
                    else:
                        break
            if Option == '2':
                print('ByeBye!')
                RES = False
                break
        else:continue

