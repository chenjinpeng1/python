#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
from django import template
from django.utils.html import format_html

register = template.Library()

@register.filter
def alex_upper(val):
    print("--val from template:",val )
    return val.upper()


@register.simple_tag
def guess_page(current_page,loop_num):
    offset = abs(current_page - loop_num)
    if offset <3:
        print(current_page)
        if current_page == loop_num:

            page_ele = '''<li class="active"><a href="?page=%s">%s</a></li>''' %(loop_num,loop_num)
        else:
            page_ele = '''<li class=""><a href="?page=%s">%s</a></li>''' %(loop_num,loop_num)
        return format_html(page_ele)
    else:
        return ''