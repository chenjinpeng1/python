#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
from bbs import models
from django.forms import ModelForm
class ArticleModelForm(ModelForm):
    class Meta:
        model = models.Article
        exclude = ("pub_date",'author','priority')
    def __init__(self,*args,**kwargs):
        super(ArticleModelForm,self).__init__(*args,**kwargs)
        print("base_fields:",self.base_fields)
        for field_name in self.base_fields:
            print(field_name)
            field = self.base_fields[field_name]
            field.widget.attrs.update({'class':'form-control'})