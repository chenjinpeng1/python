from django.contrib import admin
# from django  import fo


def make_forbidden(modelAdmin,request,queryset):
    print('--->',request,queryset)
    queryset.update(status='published')
    make_forbidden.short_description = "Set to Forbidden"

#admin 定制功能
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','publisher','publish_date','status','colored_status') #显示的字段信息，# 注： 不能显示多对多字段
    search_fields = ('name','publisher__name',) #添加搜索框
    list_filter = ('publisher','publish_date',) # 过滤功能
    list_editable = ('name','publish_date',) # 前端可直接修改的字段
    list_per_page = 10 #每页内容
    filter_horizontal = ('authors',) # 针对多对多的水平筛选搜索
    raw_id_fields = ('publisher',) #搜索外键
    actions = [make_forbidden,] # d定制admin action
# Register your models here.
from books import models
admin.site.register(models.Author)
admin.site.register(models.Publisher)
admin.site.register(models.Book,BookAdmin) #BookAdmin 是将自己写的类作为参数封装到注册admin