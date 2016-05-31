# -*- encoding:utf-8 -*-
from django.shortcuts import render,HttpResponse
from books import models
import json
import datetime
from books import form_models
# Create your views here.

def index(request):
    libname = []
    libname.append(models.Book.__name__)
    libname.append(models.Author.__name__)
    libname.append(models.Publisher.__name__)
    return render(request,'book/index.html',{'libnames':libname})

def book(request):
    books = models.Book.objects.all()
    publisher_list = models.Publisher.objects.all()
    author_list = models.Author.objects.all()
    Tiers = []
    Tier = models.Book.__name__
    Tiers.append(Tier)
    return render(request, 'book/book2.html', {'books':books,
                                                  'publishers':publisher_list,
                                                 'authors':author_list,
                                                 'Tiers':Tiers,
                                                            })


def addBook(request):
    print(request.POST)
    if request.method == 'POST':
        book_name = request.POST.get('name')
        publisher_id = request.POST.get('publisher_id')
        author_ids = request.POST.getlist('author_ids')
        print(book_name,publisher_id,author_ids)
        pubdatatime = datetime.date.today()
        new_book = models.Book(
            name=book_name,
            publisher_id = publisher_id,
            publish_date = pubdatatime,
        )
        new_book.save()
        new_book.authors.add(*author_ids)
        books = models.Book.objects.all()
        publisher_list = models.Publisher.objects.all()
        author_list = models.Author.objects.all()
        return render(request, 'book/book2.html', {'books':books,
                                                  'publishers':publisher_list,
                                                 'authors':author_list
                                                            })
    elif request.method == 'GET':
        publisher_list = models.Publisher.objects.all()
        author_list = models.Author.objects.all()
        return render(request,'book/Add_Book.html',{'publishers':publisher_list,
                                                    'authors':author_list})

def addauthor(request):
    if request.method == 'POST':
        print(request.POST)
        FirstName = request.POST.get("firstname")
        LastName = request.POST.get("lastname")
        Email = request.POST.get("email")
        print(FirstName,LastName,Email)
        models.Author.objects.create(first_name=FirstName,last_name=LastName,email=Email)
        Authors = models.Author.objects.all()
        Tiers = []
        Tier = models.Author.__name__
        Tiers.append(Tier)
        return render(request,'author/Author.html',{'Authors':Authors,
                                                    'Tiers':Tiers})

    elif request.method == 'GET':
        return render(request,'author/AddAuthor.html')

def Author(request):
    Authors = models.Author.objects.all()
    Tiers = []
    Tier = models.Author.__name__
    Tiers.append(Tier)
    return render(request,'author/Author.html',{'Authors':Authors,
                                                    'Tiers':Tiers})

def Publisher(request):
    Publisher = models.Publisher.objects.all()
    Tiers = []
    Tier = models.Publisher.__name__
    Tiers.append(Tier)
    return render(request,'publisher/Publisher.html',{'publishers':Publisher,
                                                            'Tiers':Tiers})

def addPublisher(request):
    if request.method == "POST":
        print(request.POST)
        name=request.POST.get("name")
        address=request.POST.get("address")
        city=request.POST.get("city")
        state_province=request.POST.get("state_province")
        country=request.POST.get("county")
        website=request.POST.get("website")
        models.Publisher.objects.create(name=name,address=address,city=city,state_province=state_province,country=country,website=website)
    return render(request,'publisher/AddPublisher.html')

def forms(request):
    Forms = form_models.BookForm()
    if request.method == 'POST':
        print(request.POST)
        Forms = form_models.BookForm(request.POST)
        if Forms.is_valid():
            print("form is ok")
            form_data = Forms.cleaned_data
            print('form1---',form_data)
            form_data['publisher_id'] = request.POST.get('publisher_id')
            print('form2---',form_data)
            book_obj = models.Book(**form_data)
            book_obj.save()
        else:
            print(Forms.errors)
    publisher_list = models.Publisher.objects.all()
    return render(request,'formspage/forms.html',{'forms':Forms,
                                                  "publishers":publisher_list})


def book_modelform(request):
    form = form_models.ModelForm()
    print(form)
    if request.method == "POST":
        print(request.POST)
        form = form_models.ModelForm(request.POST)
        if form.is_valid():
            print("form is ok")
            form.save()
    print(form.errors)
    return render(request,'formspage/modelform.html',{"forms":form})

