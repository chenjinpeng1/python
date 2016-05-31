#python 3.5环境,解释器在linux需要改变
# -*- encoding:utf-8 -*-
#Auth  ChenJinPeng
from django import forms
from crm import models
def get_form(classname,*args,**kwargs):
    # def __init__(self):
    #     super(ModelForm, self).__init__(*args, **kwargs)
    #     print("aaa")
    class ModelForm(forms.ModelForm):
        class Meta:
            model = classname
            exclude = ()
            # widgets = {
            #         'name':forms.TextInput(attrs={'class':"form_control"}), # name字段加样式
            #     }
        # def __init__(self,*args,**kwargs):
        #     super(ModelForm,self).__init__(*args,**kwargs)
        #     print("bbbbb")
    return ModelForm(*args,**kwargs)
