#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li


class BaseSaltModule(object):
    def __init__(self,sys_argvs,db_models,settings):
        self.db_models = db_models
        self.settings = settings
        self.sys_argvs = sys_argvs

    def get_selected_os_types(self):#获取系统类型
        data = {}
        for host in self.host_list:
            data[host.os_type] = [host]
        print('--->data',data)
        return data
    def process(self): # 提取主机信息
        self.fetch_hosts() #获取主机
        self.config_data_dic = self.get_selected_os_types() # 获取主机操作系统类型。格式： {'windows': [<Host: windows test>], 'ubuntu': [<Host: ubuntu test>]}
    def require(self,*args,**kwargs):#所有配置文件都有可能出现的配置
        if args:
            print('require',args)
        else:
            print('require',kwargs)
    def fetch_hosts(self):
        '''
        提取主机
        :return:
        '''
        print('--fetching hosts---')
        #判断相对应操作
        if '-h' in self.sys_argvs or '-g' in self.sys_argvs:
            host_list = []
            if '-h' in self.sys_argvs:
                host_str_index = self.sys_argvs.index('-h') +1 #-h后跟主机名
                if len(self.sys_argvs) <= host_str_index: # 如果-h后没跟主机 退出抛出错误
                    exit("host argument must be provided after -h")
                else: #get the host str
                    host_str = self.sys_argvs[host_str_index] # 获取主机
                    host_str_list = host_str.split(',') #可能存在多个主机，所以转换列表
                    host_list += self.db_models.Host.objects.filter(hostname__in=host_str_list) # 数据库查询存在的主机，依次添加到主机列表 注: 这里是不是如果主机不存在退出抛错更好些
            elif '-g' in self.sys_argvs:
                group_str_index = self.sys_argvs.index('-g') +1
                if len(self.sys_argvs) <= group_str_index:
                    exit("group argument must be provided after -g")
                else: #get the group str
                    group_str = self.sys_argvs[group_str_index]
                    group_str_list = group_str.split(',')
                    group_list = self.db_models.HostGroup.objects.filter(name__in=group_str_list) # 查询在列表中的组对象
                    for group in group_list: # 获取主机
                        host_list += group.hosts.select_related()
            else:exit("host is no exit!")
            self.host_list = set(host_list) # 集合去重
            return True
        else:
            exit("host [-h] or group[-g] argument must be provided")

    def syntax_parser(self,section_name,mod_name,mod_data):
        '''
        模块检查
        :param section_name:
        :param mod_name:
        :param mod_data:
        :return:
        '''
        print("-going to parser state data:",section_name,"|",mod_name,'|',mod_data)
        for state_item in mod_data:
            # print("\t",state_item)
            for key,val in state_item.items():
                if hasattr(self,key):
                    state_func = getattr(self,key)
                    state_func(val)
                else:
                    exit("Error:module [%s] has no argument [%s]" %( mod_name,key ))
        return True
        print('-------------model_name:',mod_name)
