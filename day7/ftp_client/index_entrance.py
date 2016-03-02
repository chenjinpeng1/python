#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
import sys,os
DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR)
import ftp-client
# import configparser
# config = configparser.ConfigParser()
# config.read("../ftp_server/ftp.config")
# config["FTP CONFIG FILE"] = {}
# config["USER / PASS"] = {}
# config["USER / PASS"]["chen"] = "123"
# with open("../ftp_server/ftp.config","w") as f:
#     config.write(f)



if __name__ == "__main__":
    # print("-----------------------欢迎使用ftp客户端程序------------------------------------")
    Login = input("Logining in system user:")
    Login_Passwd = input("Logining in system Passwd:")
    if Login in config["USER / PASS"] and Login_Passwd == config["USER / PASS"][Login]:
        print("Welcome you,[%s]"%Login)
        print("help查看使用帮助,不然你会为你的无知让我付出代价")




    else:print("Password Error.....")
