#!/usr/bin/env python3.5
import getpass
import configparser
import os,sys
DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR)
print(DIR)
def LOGIN():
	USER=input("User：").strip()
	PASSWD=input("PASSWD:").strip()
	info = configparser.ConfigParser()
	info.read("../log/user.conf")

	if USER in info["auth"]:
		if PASSWD == info["auth"][USER]:
			return True
	else:
		print(info["chen"])
		return False		
def REGISTERED():
	USER=input("User:").strip()
	PASSWD=input("PASSWD:").strip()
	info = configparser.ConfigParser()
	info["auth"]={}
	info["auth"]["chen"]=""
	with open("../log/user.conf","a") as f:
    		info.write(f)
	return True

