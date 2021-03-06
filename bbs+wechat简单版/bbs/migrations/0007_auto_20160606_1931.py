# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-06 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0006_auto_20160606_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='head_img',
            field=models.ImageField(default=1, height_field=150, upload_to='uploads', verbose_name='头像', width_field=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='signature',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='签名'),
        ),
    ]
