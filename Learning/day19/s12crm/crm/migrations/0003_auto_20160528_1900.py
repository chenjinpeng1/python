# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 11:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20160528_1859'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'permissions': (('can_del_customer', '\u53ef\u4ee5\u5220\u9664\u7528\u6237'),)},
        ),
    ]
