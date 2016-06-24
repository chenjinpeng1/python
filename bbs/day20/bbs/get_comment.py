#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
import os
from django.db.models import Count
from django.db.models import F,Q
os.environ['DJANGO_SETTINGS_MODULE']='s12bbs.settings'
import django
django.setup()
from bbs import models
import collections
def find_parent_comment(com_tree,comment_obj):
    for k,v in com_tree.items():
        if k == comment_obj.parent_comment: # 如果字典里的k == 当前循环的对象的父亲 代表找到当前循环的对象是他的儿子
            com_tree[k][comment_obj] = {}
        else: # 否则
            find_parent_comment(com_tree[k],comment_obj)
def get_comment(comment_obj):
    comment_tree = collections.OrderedDict()
    for comment in comment_obj:
        if comment.parent_comment is None:
            comment_tree[comment] = {}
            print(comment.user)
        else:
            find_parent_comment(comment_tree,comment)
    return comment_tree
#
# from bbs import models
# username = models.User.objects.get(username="chen")
# print(username.userprofile.name)
