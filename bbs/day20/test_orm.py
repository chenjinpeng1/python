#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 's12bbs.settings'
import django
django.setup()
from bbs import models
Search_Article = models.Article.objects.get(title='东京夜晚的故事')
print(Search_Article)
all_comment = Search_Article.comment_set.select_related() # 反向从文章查询评论数
print(all_comment)
comment_tree = {}
def find_parent_comment(com_tree,comment_obj):
    print('循环开始的字典---%s'%com_tree)
    for k,v in com_tree.items():
        if k == comment_obj.parent_comment: # 如果字典里的k == 当前循环的对象的父亲 代表找到当前循环的对象是他的儿子
            print('我是%s,我的儿子是%s'%(k,comment_obj))
            com_tree[k][comment_obj] = {}
        else: # 否则吧
            print('迭代查找的字典----%s'%com_tree[k])
            find_parent_comment(com_tree[k],comment_obj)
for comment in all_comment:
    if comment.parent_comment is None:
        print('------None',comment,type(comment))
        comment_tree[comment] = {}
        print('我是顶层%s---%s'%(comment,comment_tree))
    else:
        print('----不是顶层',comment,comment.parent_comment)
        print('返回去的字典---%s---数据%s'%(comment_tree,comment))
        find_parent_comment(comment_tree,comment)
print('-----------------------')
for k,v in comment_tree.items():
    print(k,v)
print('-----------------------')
