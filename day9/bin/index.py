import sys,os
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE)
from modules import cmd
def help():
    print("""
    argv[1] is "GroupName"
    argv[2] is Modules.func
    argv[3] is "command" | "remote_path,local_path"
    """)
if __name__=="__main__":
    try:
        args=sys.argv[1:]
        if len(args) == 1:
            assert args[0] == "help"
            print("Help 帮助菜单")
            help()
        else:
            assert len(args) == 3
            modles=args[1].split(".")[0] #获取模板名
            funcs=args[1].split(".")[1] # 获取方法名
            modle=__import__("modules.%s"%modles) #____import__函数 是把用户输入的字符串转换为模块,因为不在同级目录，所在需要加上目录名
            # print(modle)
            modle_func=getattr(modle,modles) # 获取模板下的类
            # print(modle_func)
            func_slh=getattr(modle_func,modles) # 获取类下的方法
            # print(func_slh)
            A=func_slh(*args) #实例化
            B=getattr(A,funcs) #
            # B() #类里为对象设置了属性 不用加括号直接调用
    except (IndexError,AttributeError,AssertionError) as e:
        print("参数错误")
        print(e)
        help()
