from django.db import models

# Create your models here.
# from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.

# @python_2_unicode_compatible
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tag_line = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name
# @python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    class Meta:
        verbose_name = '认证名字'#verbose_name的意思很简单，就是给你的模型类起一个更可读的名字
        verbose_name_plural = '认证名字'#如果不指定Django会自动在模型名称后加一个’s’

    def __str__(self):              # __unicode__ on Python 2
        return self.name
# @python_2_unicode_compatible
class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return self.headline
