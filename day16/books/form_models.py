#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
from django import forms
from books import models
class BookForm(forms.Form):
    name = forms.CharField(max_length=10)
    publish_date = forms.DateField()

class ModelForm(forms.ModelForm):
    class Meta:
        model = models.Book
        # fields = ('name','publish_date') #选择指定关联字段在前端显示
        exclude = ()# 如果不指定选择显示的字段，必须指定exclude ，选择不显示的字段 空表示无
        widgets = {
            'name':forms.TextInput(attrs={'class':"form_control"}), # name字段加样式
        }