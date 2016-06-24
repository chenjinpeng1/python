from django.contrib import admin
from BBS import models
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','category','author','pub_date','last_modify','status','priority')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article','parent_comment','comment_type','comment','user','date')
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','set_as_top_menu','position_index')

# Register your models here.
admin.site.register(models.Article,ArticleAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.UserProfile)
admin.site.register(models.Category,CategoryAdmin)
