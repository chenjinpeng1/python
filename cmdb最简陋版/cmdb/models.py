from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    Mobile = models.IntegerField(max_length=11)
    Email = models.CharField(max_length=32)
    def __str__(self):
        return '%s' %(self.username)

class HostInfo(models.Model):
    id = models.AutoField(primary_key=True, )
    hostname = models.CharField(max_length=32)
    ip = models.GenericIPAddressField()
    port = models.IntegerField(max_length=5)
    def __str__(self):
        return '%s '%(self.hostname)


