
from django.conf.urls import url,include
from webchat import views
urlpatterns = [
    url(r'^$', views.dashboard,name='chat_dashboard'),
    url(r'^msg_send/$', views.send_msg,name='send_msg'),
    url(r'^new_msgs/$', views.get_new_msgs,name='get_new_msgs'),
    url(r'^file_upload/$', views.file_upload,name='file_upload'),
    url(r'^file_upload_progress/$', views.get_file_upload_progress,name='file_upload_progress'),
    url(r'^delete_cache_key/$', views.delete_cache_key,name='delete_cache_key'),
    url(r'^info_search/$', views.info_search,name='search_info'),
    url(r'^Add_Friend/$', views.Add_Friend,name='Add_Friend'),
    url(r'^Confirm_add_user/$', views.Confirm_add_user,name='Confirm_add_user'),
]
