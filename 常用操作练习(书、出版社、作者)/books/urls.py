from django.conf.urls import url,include
from books import views
urlpatterns = [
    url(r'Book/$',views.book),
    url(r'index/$',views.index),
    url(r'^addBook/$',views.addbook),
    url(r'^Author/$',views.Author),
    url(r'^addAuthor/$',views.addauthor),
    url(r'^Publisher/$',views.Publisher),
]
