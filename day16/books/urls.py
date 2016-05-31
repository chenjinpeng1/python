from django.conf.urls import url,include
from books import views
urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^Book/$',views.book),
    url(r'^addBook/$',views.addBook),
    url(r'^Author/$',views.Author),
    url(r'^addAuthor/$',views.addauthor),
    url(r'^Publisher/$',views.Publisher),
    url(r'^addPublisher/$',views.addPublisher),
    url(r'^forms/$',views.forms),
    url(r'^modelforms/$',views.book_modelform),
]
