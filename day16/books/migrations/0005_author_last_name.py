# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-20 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_remove_author_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(default='', max_length=32),
        ),
    ]
