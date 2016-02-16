#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
import pickle,os,sys
DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR)
def Write(info):
    File=open('Card/config.txt','wb')
    File.write(pickle.dumps(info))
    File.close()
def Read():
    File=open('Card/config.txt','rb')
    info=pickle.loads(File.read())
    File.close()
    return info
def Write_XF(log):
    File=open('Card/xiaofei.txt','a')
    File.write(log)
    File.close()
def Read_XF():
    File=open('Card/xiaofei.txt','r')
    info=File.read()
    print(info)
    File.close()


