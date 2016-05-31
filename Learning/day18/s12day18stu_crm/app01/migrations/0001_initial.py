# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_type', models.CharField(max_length=32, verbose_name='\u8bfe\u7a0b\u7c7b\u578b', choices=[(b'online', '\u7f51\u7edc\u73ed'), (b'offline_weekend', '\u9762\u6388\u73ed(\u5468\u672b)'), (b'offline_fulltime', '\u9762\u6388\u73ed(\u8131\u4ea7)')])),
                ('semester', models.IntegerField(verbose_name='\u5b66\u671f')),
                ('start_date', models.DateField(verbose_name='\u5f00\u73ed\u65e5\u671f')),
                ('graduate_date', models.DateField(null=True, verbose_name='\u7ed3\u4e1a\u65e5\u671f', blank=True)),
            ],
            options={
                'verbose_name': '\u73ed\u7ea7\u5217\u8868',
                'verbose_name_plural': '\u73ed\u7ea7\u5217\u8868',
            },
        ),
        migrations.CreateModel(
            name='ConsultRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.TextField(verbose_name='\u8ddf\u8fdb\u5185\u5bb9...')),
                ('status', models.IntegerField(help_text='\u9009\u62e9\u5ba2\u6237\u6b64\u65f6\u7684\u72b6\u6001', verbose_name='\u72b6\u6001', choices=[(1, '\u8fd1\u671f\u65e0\u62a5\u540d\u8ba1\u5212'), (2, '2\u4e2a\u6708\u5185\u62a5\u540d'), (3, '1\u4e2a\u6708\u5185\u62a5\u540d'), (4, '2\u5468\u5185\u62a5\u540d'), (5, '1\u5468\u5185\u62a5\u540d'), (6, '2\u5929\u5185\u62a5\u540d'), (7, '\u5df2\u62a5\u540d')])),
                ('date', models.DateField(auto_now_add=True, verbose_name='\u8ddf\u8fdb\u65e5\u671f')),
            ],
            options={
                'verbose_name': '\u5ba2\u6237\u54a8\u8be2\u8ddf\u8fdb\u8bb0\u5f55',
                'verbose_name_plural': '\u5ba2\u6237\u54a8\u8be2\u8ddf\u8fdb\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128, verbose_name='\u8bfe\u7a0b\u540d\u79f0')),
                ('price', models.IntegerField(verbose_name='\u9762\u6388\u4ef7\u683c')),
                ('online_price', models.IntegerField(verbose_name='\u7f51\u7edc\u73ed\u4ef7\u683c')),
                ('brief', models.TextField(verbose_name='\u8bfe\u7a0b\u7b80\u4ecb')),
            ],
        ),
        migrations.CreateModel(
            name='CourseRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day_num', models.IntegerField(help_text='\u6b64\u5904\u586b\u5199\u7b2c\u51e0\u8282\u8bfe\u6216\u7b2c\u51e0\u5929\u8bfe\u7a0b...,\u5fc5\u987b\u4e3a\u6570\u5b57', verbose_name='\u8282\u6b21')),
                ('date', models.DateField(auto_now_add=True, verbose_name='\u4e0a\u8bfe\u65e5\u671f')),
                ('course', models.ForeignKey(verbose_name='\u73ed\u7ea7(\u8bfe\u7a0b)', to='app01.ClassList')),
            ],
            options={
                'verbose_name': '\u4e0a\u8bfe\u7eaa\u5f55',
                'verbose_name_plural': '\u4e0a\u8bfe\u7eaa\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qq', models.CharField(unique=True, max_length=64, verbose_name='QQ\u53f7')),
                ('name', models.CharField(max_length=32, null=True, verbose_name='\u59d3\u540d', blank=True)),
                ('phone', models.BigIntegerField(null=True, verbose_name='\u624b\u673a\u53f7', blank=True)),
                ('stu_id', models.CharField(max_length=64, null=True, verbose_name='\u5b66\u53f7', blank=True)),
                ('source', models.CharField(default=b'qq', max_length=64, verbose_name='\u5ba2\u6237\u6765\u6e90', choices=[(b'qq', 'qq\u7fa4'), (b'referral', '\u5185\u90e8\u8f6c\u4ecb\u7ecd'), (b'51cto', '51cto'), (b'agent', '\u62db\u751f\u4ee3\u7406'), (b'others', '\u5176\u5b83')])),
                ('class_type', models.CharField(max_length=64, verbose_name='\u73ed\u7ea7\u7c7b\u578b', choices=[(b'online', '\u7f51\u7edc\u73ed'), (b'offline_weekend', '\u9762\u6388\u73ed(\u5468\u672b)'), (b'offline_fulltime', '\u9762\u6388\u73ed(\u8131\u4ea7)')])),
                ('customer_note', models.TextField(help_text='\u5ba2\u6237\u54a8\u8be2\u7684\u5927\u6982\u60c5\u51b5,\u5ba2\u6237\u4e2a\u4eba\u4fe1\u606f\u5907\u6ce8\u7b49...', verbose_name='\u5ba2\u6237\u54a8\u8be2\u5185\u5bb9\u8be6\u60c5')),
                ('status', models.CharField(default='unregistered', help_text='\u9009\u62e9\u5ba2\u6237\u6b64\u65f6\u7684\u72b6\u6001', max_length=64, verbose_name='\u72b6\u6001', choices=[(b'signed', '\u5df2\u62a5\u540d'), (b'unregistered', '\u672a\u62a5\u540d'), (b'graduated', '\u5df2\u6bd5\u4e1a')])),
                ('date', models.DateField(auto_now_add=True, verbose_name='\u54a8\u8be2\u65e5\u671f')),
                ('class_list', models.ManyToManyField(to='app01.ClassList', verbose_name='\u5df2\u62a5\u73ed\u7ea7', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64, verbose_name='\u6821\u533a\u540d\u79f0')),
                ('addr', models.CharField(max_length=128, verbose_name='\u5730\u5740')),
            ],
        ),
        migrations.CreateModel(
            name='StudyRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('record', models.CharField(default=b'checked', max_length=64, verbose_name='\u4e0a\u8bfe\u7eaa\u5f55', choices=[(b'checked', '\u5df2\u7b7e\u5230'), (b'late', '\u8fdf\u5230'), (b'noshow', '\u7f3a\u52e4'), (b'leave_early', '\u65e9\u9000')])),
                ('score', models.IntegerField(default=-1, verbose_name='\u672c\u8282\u6210\u7ee9', choices=[(100, b'A+'), (90, b'A'), (85, b'B+'), (80, b'B'), (70, b'B-'), (60, b'C+'), (50, b'C'), (40, b'C-'), (0, b'D'), (-1, b'N/A'), (-100, b'COPY'), (-1000, b'FAIL')])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('note', models.CharField(max_length=255, null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('course_record', models.ForeignKey(verbose_name='\u7b2c\u51e0\u5929\u8bfe\u7a0b', to='app01.CourseRecord')),
                ('student', models.ForeignKey(verbose_name='\u5b66\u5458', to='app01.Customer')),
            ],
            options={
                'verbose_name': '\u5b66\u5458\u5b66\u4e60\u7eaa\u5f55',
                'verbose_name_plural': '\u5b66\u5458\u5b66\u4e60\u7eaa\u5f55',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u59d3\u540d')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='school',
            name='staffs',
            field=models.ManyToManyField(to='app01.UserProfile', blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='consultant',
            field=models.ForeignKey(verbose_name='\u8bfe\u7a0b\u987e\u95ee', to='app01.UserProfile'),
        ),
        migrations.AddField(
            model_name='customer',
            name='course',
            field=models.ForeignKey(verbose_name='\u54a8\u8be2\u8bfe\u7a0b', to='app01.Course'),
        ),
        migrations.AddField(
            model_name='customer',
            name='referral_from',
            field=models.ForeignKey(related_name='internal_referral', blank=True, to='app01.Customer', help_text='\u82e5\u6b64\u5ba2\u6237\u662f\u8f6c\u4ecb\u7ecd\u81ea\u5185\u90e8\u5b66\u5458,\u8bf7\u5728\u6b64\u5904\u9009\u62e9\u5185\u90e8\u5b66\u5458\u59d3\u540d', null=True, verbose_name='\u8f6c\u4ecb\u7ecd\u81ea\u5b66\u5458'),
        ),
        migrations.AddField(
            model_name='courserecord',
            name='teacher',
            field=models.ForeignKey(verbose_name='\u8bb2\u5e08', to='app01.UserProfile'),
        ),
        migrations.AddField(
            model_name='consultrecord',
            name='consultant',
            field=models.ForeignKey(verbose_name='\u8ddf\u8e2a\u4eba', to='app01.UserProfile'),
        ),
        migrations.AddField(
            model_name='consultrecord',
            name='customer',
            field=models.ForeignKey(verbose_name='\u6240\u54a8\u8be2\u5ba2\u6237', to='app01.Customer'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='course',
            field=models.ForeignKey(to='app01.Course'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='teachers',
            field=models.ManyToManyField(to='app01.UserProfile', verbose_name='\u8bb2\u5e08'),
        ),
        migrations.AlterUniqueTogether(
            name='studyrecord',
            unique_together=set([('course_record', 'student')]),
        ),
        migrations.AlterUniqueTogether(
            name='courserecord',
            unique_together=set([('course', 'day_num')]),
        ),
        migrations.AlterUniqueTogether(
            name='classlist',
            unique_together=set([('course', 'course_type', 'semester')]),
        ),
    ]
