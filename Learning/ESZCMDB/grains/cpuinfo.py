#!/bin/env python
# -*- encoding:utf-8 -*-
#python 3.5环境,解释器在linux需要改变
#Auth  ChenJinPeng
import subprocess

def disk():
    disk_count = subprocess.Popen('fdisk -l | sed -rn "s#Disk (/dev/xvd[a-z]).*#\1#p"',shell=True,stdout=subprocess.PIPE)
