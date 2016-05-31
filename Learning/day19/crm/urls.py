
from django.conf.urls import url,include
from  crm import views
urlpatterns = [
    url(r'^$', views.dashboard),
    url(r'^customer$', views.customer),
]
