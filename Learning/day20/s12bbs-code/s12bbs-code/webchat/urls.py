
from django.conf.urls import url,include
from webchat import views
urlpatterns = [
    url(r'^$', views.dashboard,name='chat_dashboard'),
    url(r'^msg_send/$', views.send_msg,name='send_msg'),
    url(r'^new_msgs/$', views.get_new_msgs,name='get_new_msgs'),
    # url(r'^new_msgs_counts/$', views.get_new_msgs_counts,name='get_new_msgs_counts'),
]
