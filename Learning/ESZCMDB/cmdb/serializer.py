#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng

from cmdb import models
from rest_framework import serializers, viewsets, routers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('url', 'email', 'name', 'is_staff')

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Asset
        fields = ('url', 'sn', 'assert_type', 'manufactory','name','create_date')

class ManufactorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Manufactory
        fields = ('url', 'manufactory', 'support_num', 'memo')

