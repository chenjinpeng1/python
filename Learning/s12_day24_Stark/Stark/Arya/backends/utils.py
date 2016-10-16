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
        self.argv_parse()  # 初始化执行参数解析

    def help_msg(self):
        '''
        帮助文档
        :return:
        '''
        print("Available modules:")
        for registered_module in action_list.actions:
            print("  %s" % registered_module)
        exit()
    def argv_parse(self):
        '''
        参数解析分发
        :return:
        '''
        #print(self.argvs)
        if len(self.argvs) <2:
            self.help_msg()
        module_name = self.argvs[1]
        if '.' in module_name: #state.apply
            mod_name,mod_method = module_name.split('.')
            module_instance  = action_list.actions.get(mod_name) #获取字典内参数对应的模块
            if module_instance:#matched 模块
                module_obj = module_instance(self.argvs,models,settings) #实例化了State()
                if hasattr(module_obj,mod_method):
                    module_method_obj = getattr(module_obj,mod_method)#解析任务，发送到队列，取任务结果
                    module_obj.process() #提取 主机
                    module_method_obj() #调用指定的指令 # State().apply()
                    # module_obj.process() #提取 主机
                else:
                    exit("module [%s] doesn't have [%s] method" % (mod_name,mod_method))
            else:
                exit("invalid module name argument")
        else:
            exit("模块没有相对应的参数")

