# -*- encoding:utf-8 -*-
from django.shortcuts import render,HttpResponse
from books import models
import json
import datetime
# Create your views here.
# def book(request):
#     if request.method =='POST':
#         book_name = request.POST['name']
#         publisher_id = request.POST['publisher_id']
#         author_ids = request.POST.getlist('author_id')
#         current_time = datetime.date.today()
#         print(book_name,publisher_id,author_ids)
#         print(request.POST)
#         models.Book.objects.create(name=book_name,publisher_id=publisher_id,publish_date=current_time)
#     books = models.Book.objects.all()
#     author_list = models.Author.objects.all()
#     publisher_list = models.Publisher.objects.all()
#     return render(request,'book/index.html',{'books':books,
#                                          'publishers':publisher_list,
#                                              'authors':author_list})


def book(request):

    if request.method == 'POST':
        print(request.POST)
        book_name = request.POST.get('name')
        publisher_id = request.POST.get('publisher_id')
        author_ids = request.POST.getlist('author_ids')
        print(book_name,publisher_id,author_ids)

        new_book = models.Book(
            name=book_name,
            publisher_id = publisher_id,
            publish_date = '2016-05-22'
        )
        new_book.save()
        new_book.authors.add(*author_ids)
        #new_book.authors.add(1,2,3,4)
    test = models.Book.__name__
    print(test)
    books = models.Book.objects.all()
    print(books,type(books))
    publisher_list = models.Publisher.objects.all()
    author_list = models.Author.objects.all()
    return render(request, 'book/book2.html', {'books':books,
                                                  'publishers':publisher_list,
                                                 'authors':author_list
                                                            })

def index(request):
    libname = []
    libname.append(models.Book.__name__)
    libname.append(models.Author.__name__)
    libname.append(models.Publisher.__name__)
    print(libname)

    return render(request,'book/index.html',{'libnames':libname})


def addbook(request):
    publisher_list = models.Publisher.objects.all()
    author_list = models.Author.objects.all()
    return render(request,'book/Add_Book.html',{'publishers':publisher_list,
                                                'authors':author_list})


def addauthor(request):
    if request.method == 'post':
        print(request.POST)

def Author(request):
    Authors = models.Author.objects.all()

    return render(request,'author/Author.html',{'Authors':Authors})

def Publisher(request):
    Publisher = models.Publisher.objects.all()
    return render(request,'publisher/Publisher.html',{'publishers':Publisher})
