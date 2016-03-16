#/usr/bin/env python3
#-*-encoding:utf8-*-
import sys,os
class CMD(object):
    @staticmethod
    def help(self):
        '''
        CMD.run  -运行命令
        CMD.get -下载文件
        CMD.put -上传文件
        '''
    def run(self):
        print("run")
    def get(self):
        print("get")
        pass
    def put(self):
        print("put")
        pass


    # def


if __name__ == "__main__":
    A=sys.argv[1:] # 格式为[group,cmd.* command|filename]
    print(A)
    try:
        assert len(A) ==3
        CLASS=A[1].split(".")[0]
        FUNC=A[1].split(".")[1]
        print(CLASS,FUNC)
    except AssertionError as e:
        print("参数错误")
        print(e)

