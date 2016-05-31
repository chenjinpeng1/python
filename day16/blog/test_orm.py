#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
# 创建一个py脚本来来方便调试增删改查
import os
from django.db.models import F,Q,Count,Sum,Avg,Min,Max
os.environ['DJANGO_SETTINGS_MODULE']='day16.settings' #将setting模板加入环境变量
import django # 导入django
django.setup()
from blog import models
 # foreignkey关联
# entry = models.Entry.objects.get(pk=1) # 查询主键为1
# print(entry.blog)
# blog = models.Blog.objects.get(id=2)
# print(blog)
# entry.blog = blog
# entry.save()

 # manytomany关联
# NZ = models.Author.objects.create(name='小哪吒')
# LH = models.Author.objects.create(name='老虎')
# entry.authors.add(NZ,LH)

# 单表内查询语句链式查询
#all_entries = Entry.objects.all() #查询所有
# Entry.objects.filter(pub_date__year=2006) #查询所有pub_date为2006年的纪录
# Entry.objects.all().filter(pub_date__year=2006) #与上面那句一样
# >>> Entry.objects.filter(   #链式查询
# ...     headline__startswith='What'
# ... ).exclude(
# ...     pub_date__gte=datetime.date.today()
# ... ).filter(
# ...     pub_date__gte=datetime(2005, 1, 30)
# ... )
#
# one_entry = Entry.objects.get(pk=1) #单条查询
#
# Entry.objects.all()[:5] #查询前5条
# Entry.objects.all()[5:10] #查询第五条-第十条
#
# Entry.objects.order_by('headline')[0] #按headline排序取第一条
#obj = models.Entry.objects.get(blog__name__contains='生活') 查找出blog字段中对应的外键Blog name=生活的板块
# Entry.objects.filter(pub_date__lte='2006-01-01') #相当于sql语句SELECT * FROM blog_entry WHERE pub_date <= '2006-01-01';
#
# Entry.objects.get(headline__exact="Cat bites dog") #相当于SELECT ... WHERE headline = 'Cat bites dog';
# Blog.objects.get(name__iexact="beatles blog") #与上面相同,只是大小写不敏感
#
# Entry.objects.get(headline__contains='Lennon') #相当 于SELECT ... WHERE headline LIKE '%Lennon%';
#


# objs = models.Entry.objects.filter(n_comments__lte=F('n_pingbacks'))
# print(objs)
# addblog = models.Blog.objects.create(name='python')
objs = models.Entry.objects.filter(Q(mod_date=('2016-05-21')) and Q(n_comments__lt=F('n_pingbacks')) | Q(pub_date__lt='2016-05-17'))
print(objs)
# print(models.Entry.objects.all().aggregate(Avg('n_pingbacks'),
#                                            Sum('n_pingbacks'),
#                                            Min('n_pingbacks')
#                                            ))
# print('=============================')
from books import models as book_models
# pub_obj = book_models.Publisher.objects.first()
# print(pub_obj.name,pub_obj.book_set.select_related())# 反向关联查询 #book_set是反向关联自动生成的一个字段
# print("=================================")
# pub_objs = book_models.Publisher.objects.annotate(book_nums=Count('book')) #分类聚合
# for publisher in pub_objs:
#     print(publisher.book_nums)
objs = book_models.Book.objects.values_list('publish_date').annotate(Count('publish_date'))
for i in objs:
    print(i)

