#!/bin/env python
# -*- encoding:utf-8 -*-
#python 3.5环境,解释器在linux需要改变
#Auth  ChenJinPeng
import subprocess
def grains_asset():
    get_value = ['Manufacturer','Serial Number','UUID']
    data = {}
    for key in get_value:
        obj = subprocess.Popen("sudo dmidecode -t system | grep '%s'"%key,shell=True,stdout=subprocess.PIPE)
        obj_data = obj.stdout.read()
        data[key] = obj_data.strip().split(":")[1]
    print(data)

a,b,c = "a","b","c"
print(a,b,c)