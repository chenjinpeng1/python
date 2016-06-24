from django.test import TestCase

# Create your tests here.
import os
from django.db.models import F,Q
os.environ['DJANGO_SETTINGS_MODULE']='s12bbs.settings'
import django
django.setup()
import datetime,time
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
a=[1]
if a:
    print("bushikong")