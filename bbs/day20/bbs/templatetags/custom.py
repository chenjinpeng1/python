#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

from django import template
from django.utils.html import format_html

register = template.Library()

@register.filter
def truncate_url(img_obj):

    return  img_obj.name.split("/",maxsplit=1)[-1]


@register.simple_tag
def filter_comment(article_obj):
    print(article_obj)
    query_set = article_obj.comment_set.select_related()
    comments = {
        'comment_count': query_set.filter(comment_type=1).count(),
        'thumb_count': query_set.filter(comment_type=2).count(),
    }
    return comments

def comment_count(comment_obj):
    comment_all = comment_obj.my_children.all()
    comments = {
        'comment_count':comment_all.filter(comment_type=1).count(),
        'thumb_count': comment_all.filter(comment_type=2).count(),
    }
    return comments
def recursive_build_tree(comment_html,comment_tree,margin_num):
    for k,v in comment_tree.items():
        comment_counts = comment_count(k)
        img = truncate_url(k.user.head_img)
        first_row = '''
        <hr/>
        <div class="A-comment">
        <div class="pl-box-wrap" style='margin-left:%spx'>
        <div>
            <span style="margin-right:20px"><img class="small_img" src="/static/%s"></span>
            <span name=author_user style="margin-right:20px">%s</span>
            <span style="margin-right:20px">%s</span>

        </div>
        <div class="pl-content" style='margin-top:20px'>
            <span >%s</span>
            <span style="padding-right:20px" class='glyphicon glyphicon-thumbs-up pull-right'> %s</span>
            <span style="padding-right:20px" class='glyphicon glyphicon-comment pull-right'> %s</span>
        </div>
        <div class="glyphicon glyphicon-pencil add_comment" style="color:#666">
        我要点评
        </div>
        </div>
        </div>
        '''%(margin_num,img,k.user,k.date.strftime('%Y-%m-%d %T'),k.comment,comment_counts['thumb_count'],comment_counts['comment_count'])
        comment_html+=first_row
        if v:
            comment_html=recursive_build_tree(comment_html,comment_tree[k],margin_num+30)
    return comment_html

@register.simple_tag
def build_comment_tree(comment_tree):
    comment_html = '<div class="comment">'
    for k,v in comment_tree.items():
        comment_counts = comment_count(k)
        img = truncate_url(k.user.head_img)
        first_row = '''
        <hr/>
        <div class=A-comment>
         <div class="pl-box-wrap>
            <span style="margin-right:20px"><img class="small_img" src="/static/%s"></span>
            <span style="margin-right:20px">%s</span>
            <span style="margin-right:20px">%s</span>

            <div style='margin-top:20px'>
            <span>%s</span>
            <span style="padding-right:20px" class='glyphicon glyphicon-thumbs-up pull-right'> %s</span>
            <span style="padding-right:20px" class='glyphicon glyphicon-comment pull-right'> %s</span>
            </div>
            <div class="glyphicon glyphicon-pencil add_comment" style="color:#666">
            我要点评
            </div>
         </div>
         </div>
         '''%(img,k.user,k.date.strftime('%Y-%m-%d %T'),k.comment,comment_counts['thumb_count'],comment_counts['comment_count'])
        comment_html+=first_row
        if v:
            comment_html=recursive_build_tree(comment_html,comment_tree[k],30)
    comment_html+='</div>'
    return comment_html



