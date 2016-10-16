#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
import sys

from Arya import action_list
import django
django.setup()

from Stark import settings
from Arya import models
class ArgvManagement(object):
    '''
    接收用户指令并分配到相应模块
    '''
    def __init__(self,argvs):
        self.argvs = argvs
        self.argv_parse() # 初始化执行此方法，判断模块名称是否存在

    def help_msg(self):
        print("Available modules:")
        for registered_module in action_list.actions:
            print("  %s" % registered_module)
        exit()
    def argv_parse(self):
        if len(self.argvs) <2: # 1表示文件名
            self.help_msg()
        module_name = self.argvs[1] # 取模块.方法
        if '.' in module_name: # 格式为cmd.run
            mod_name,mod_method = module_name.split('.')
            module_instance  = action_list.actions.get(mod_name) # 从action_list字典里获取key对应的模块
            if module_instance:#matched,如果有此模块，进行实例化，传参
                module_obj = module_instance(self.argvs,models,settings) # 实例化，此形参传给基类 事例：实例化cmd.run类
                if hasattr(module_obj,mod_method): #如果模块有此方法
                    module_obj.process() #先提取主机，判断主机是否，在进行任务解析
                    module_method_obj = getattr(module_obj,mod_method)#解析任务，发送到队列，取任务结果
                    module_method_obj() #调用指定的指令
                else:
                    exit("module [%s] doesn't have [%s] method" % (mod_name,mod_method))
            else:
                self.help_msg()
        else:
            exit("invalid module name argument")

