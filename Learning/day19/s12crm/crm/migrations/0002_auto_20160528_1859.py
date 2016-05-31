# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 10:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'permissions': ('can_del_customer', '\u53ef\u4ee5\u5220\u9664\u7528\u6237')},
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='\u59d3\u540d'),
        ),
    ]
