#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
import os,sys,platform
# playform 模块获取操作系统平台


if platform.system() == "Windows":
    # BASEDIR = '\\'.join(os.path.abspath(__file__)).split('\\')[:-1]
    BASEDIR = "\\\\".join(os.path.dirname(os.path.abspath(__file__)).split("\\")[:-1])
    print('--BASEDIR:',BASEDIR)

else: #不是windows就是linux
    BASEDIR = '/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
sys.path.append(BASEDIR)
from core import ArgsInstructions

if __name__ == '__main__':
    ArgsInstructions.ArgvHandler(sys.argv)