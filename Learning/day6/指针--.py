#python 3.5环境，解释器在linux需要改变
#阅读手册查询readme文件
#作者：S12-陈金彭
with open('access.log','rb') as src:
    rd = src.read(100)
    print(rd)
    print(src.seek(src.tell()))
    rd = src.read(100)
    print(rd)
    print(src.seek(src.tell()))