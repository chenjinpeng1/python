# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-06 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0005_auto_20160606_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=32),
        ),
    ]
