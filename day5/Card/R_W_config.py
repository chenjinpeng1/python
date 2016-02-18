#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import pickle,os,sys
DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR)
A='%s%s'%(DIR,'\Card\config.txt') #读取config.txt文件
B='%s%s'%(DIR,'\Card\Xiaofei.txt') #读取xiaofei文件
C='%s%s'%(DIR,'\Card\caozuo_log.txt') #读取caozuo_log.txt文件
def Write(info):
    File=open(A,'wb')
    File.write(pickle.dumps(info))
    File.flush()
    File.close()
def Read():
    File=open(A,'rb')
    info=pickle.loads(File.read())
    File.close()
    return info
def Write_XF(log):
    File=open(B,'wb')
    File.write(pickle.dumps(log))
    File.flush()
    File.close()
def Read_XF():
    File=open(B,'rb')
    info=pickle.loads(File.read())
    File.close()
    return info
def Write_log(log):
    File=open(C,'wb')
    File.write(pickle.dumps(log))
    File.flush()
    File.close()
def Read_log():
    File=open(C,'rb')
    info=pickle.loads(File.read())
    File.close()
    return info


