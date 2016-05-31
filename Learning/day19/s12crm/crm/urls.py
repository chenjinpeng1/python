
from django.conf.urls import url,include

from crm import views
urlpatterns = [

    url(r'^$',views.dashboard ),
    url(r'^customers/$',views.customers,name="customer_list"),
    url(r'^customers/(\d+)/$',views.customer_detail,name="customer_detail" ),
]
