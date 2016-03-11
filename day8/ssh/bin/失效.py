#!/usr/bin/env python3.5
#-*-encoding:utf8 -*-
import auth

print ("欢迎来到My System！")
INDEX_LIST=["登陆","注册"]
for index,i in enumerate(INDEX_LIST,1):
	print(index,i)
USER_OPTION=input("请选择操作：")
if USER_OPTION == "1":
	RES=auth.LOGIN()
	if RES:
		print("Auth Success")
	else:
		print("Auth Faild！")
if USER_OPTION=="2":
	RES=auth.REGISTERED()
	if RES:
		pass
