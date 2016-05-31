
from django.conf.urls import url,include
from cmdb import views
urlpatterns = [
    # url(r'^cmdb/', include('cmdb.views')),
    url(r'^$', views.login),
    url(r'^login/',views.login),
    url(r'^regist/',views.regist),
    url(r'^HostManage/',views.HostManage),
    url(r'^index/',views.index),
    url(r'^selectedit/',views.selectedit),
    url(r'^AddHost/',views.AddHost),
]
