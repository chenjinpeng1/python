from django.conf.urls import url,include
from BBS import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^category/(\d+)/$', views.category),
    url(r'^login/$',views.acc_login,name='login'),
    url(r'^logout/$',views.acc_logout,name='logout'),
    url(r'^article/(\d+)$',views.ar,name='article_detail'),

]
