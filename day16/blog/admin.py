from django.contrib import admin

class entry(admin.ModelAdmin):
    list_display = ('headline','body_text','pub_date','mod_date','n_comments','n_pingbacks')
# Register your models here.
from blog import models
admin.site.register(models.Blog)
admin.site.register(models.Author)
admin.site.register(models.Entry,entry)