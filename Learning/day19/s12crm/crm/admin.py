from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.Customer)
admin.site.register(models.CustomerTrackRecord)
admin.site.register(models.ClassList)
admin.site.register(models.Course)
admin.site.register(models.CourseRecord)
admin.site.register(models.StudyRecord)
admin.site.register(models.School)