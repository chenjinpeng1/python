#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
from Arya.backends.base_module import BaseSaltModule


class Group(BaseSaltModule):
    def process_result(self):
        pass
    def gid(self,*args,**kwargs):
        print(args)
