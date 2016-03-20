#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
import select
import threading
import sys
while True:
    readable,writeable,error = select.select([sys.stdin,],[],[],1)
    if sys.stdin in readable:
        print("select get stdin:",sys.stdin)