
from django.conf.urls import url,include

from app01 import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^p1/$', views.page1),
    url(r'^p1_1/$', views.page1_1),
    url(r'^book/$', views.book),


    #url(r'cash/$', views.pay_by_cash),
    #url(r'articles/([0-9]{4})/$', views.year_archive, {'file_type':'json'}),
    #url(r'^articles/2003/$', views.special_case_2003),
    #url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+).(\w+)/$', views.article_detail),
    #url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),

    #url(r'^articles/2004/$', views.special_case_2003),
    #url(r'^articles/2005/$', views.special_case_2003),
]
