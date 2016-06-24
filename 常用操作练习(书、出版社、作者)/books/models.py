#！_*_coding:utf-8_*_
from django.db import models
import datetime
from django.contrib import admin
# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    def __str__(self):
        return "%s %s" %(self.first_name,self.last_name)

class Publisher(models.Model):
    name = models.CharField(max_length=64,unique=True)
    address = models.CharField(max_length=128,null=True,blank=True)
    city = models.CharField(max_length=64)
    state_province = models.CharField(max_length=30,help_text="put your country code here..",verbose_name=u"所属省")
    country = models.CharField(max_length=50,editable=False)
    website = models.URLField()
    def __str__(self):
        return "%s"%(self.name)

class Book(models.Model):
    name = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publish_date = models.DateField()
    def __str__(self):
        return "%s"%(self.name)