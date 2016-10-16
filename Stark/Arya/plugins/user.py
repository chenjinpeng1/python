#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
from Arya.backends.base_module import BaseSaltModule
create_user={
    'uid' :None,
    'gid':None,
    'shell':None,
    'home':None
}


class User(BaseSaltModule):
    '''
    处理掉为None的key
    '''
    def process_result(self):
        tmp=create_user.copy()
        for k,v in tmp.items():
            if v is None:
                create_user.pop(k)
        del tmp
        print('create_user_dict:---------',create_user)
        self.command()

    def uid(self,num):
        create_user['uid'] = num

    def gid(self,num):
        create_user['gid'] = num
    def shell(self,val):
        create_user['shell'] = val
    def home(self,val):
        create_user['home'] = val
    def command(self):
        '''
        生成命令字符串
        :return:
        '''
        command = 'useradd '
        if 'uid' in create_user.keys():
            command+=' %s %s'%('-u',create_user['uid'])
        if 'gid' in create_user.keys():
            command+=' %s %s'%('-g',create_user['gid'])
        if 'shell' in create_user.keys():
            command+=' %s %s'%('-s',create_user['shell'])
        if 'home' in create_user.keys():
            command+=' %s %s'%('-d',create_user['home'])
        print('RET COMMAND:------------------------------------------',command)


class UbuntuUser(User):
    def home(self,val):
        create_user['home'] = val
        self.process_result()
class RedhatUser(User):
    def home(self,val):
        create_user['home'] = val
        # self.process_result()
