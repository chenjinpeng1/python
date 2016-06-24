
from django.conf.urls import url,include
from bbs import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^category/(\d+)/$', views.category),
    url(r'^detail/(\d+)/$', views.article_detail,name="article_detail"),
    url(r'^comment/$', views.comment,name="post_comment"),
    url(r'^comment_list/(\d+)/$', views.get_comments,name="get_comments"),
    url(r'^new_article/$', views.new_article,name="new_article"),
    url(r'^new_article_count/$', views.get_new_article_count,name="get_new_article_count"),
]
