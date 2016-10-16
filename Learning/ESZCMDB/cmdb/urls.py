
from django.conf.urls import url,include
from cmdb import views
urlpatterns = [
    url(r'^asset_report/',views.assert_report,name='asset_report'),
    url(r'^$',views.ServerDashboard),
    url(r'^assets/assetslist/',views.assetslist,name='assestlist'),
    url(r'^assets/hostdetail/(\d+)',views.hostdetail,name='hostdetail'),
]
