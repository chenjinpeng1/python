from django.shortcuts import render,HttpResponse

# Create your views here.
import models
def index(request):
    if request.method == 'GET':
        user_infos = [
            {'username':'alex','name':'AlexLi'},
            {'username':'alex2','name':'AlexLi2'},
            {'username':'alex3','name':'AlexLi3'},
            {'username':'alex4','name':'AlexLi4'},
        ]
        return render(request, 'app01/index.html',{'user_objs':user_infos})
    else: #post
        return HttpResponse("transfered 100000 to alex....success.")

def page1(request):
    return  render(request,'app01/page1.html')
def page1_1(request):
    return  render(request,'app01/page1_1.html')

def pay_by_cash(request):
    return HttpResponse("Hello tuhao...")

def special_case_2003(request,user):
    print("matched 2003")


def book(request):

    if request.method == 'POST':
        print(request.POST)
        book_name = request.POST.get('name')
        publisher_id = request.POST.get('publisher_id')
        print('==>',request.POST.get('author_ids'))
        author_ids = request.POST.getlist('author_ids')
        #print(dir( request.POST))
        print(book_name,publisher_id,author_ids)

        new_book = models.Book(
            name=book_name,
            publisher_id = publisher_id,
            publish_date = '2016-05-22'
        )
        new_book.save()
        new_book.authors.add(*author_ids)
        #new_book.authors.add(1,2,3,4)

    books = models.Book.objects.all()
    publisher_list = models.Publisher.objects.all()
    author_list = models.Author.objects.all()


    return render(request,'app01/book.html',{'books':books,
                                                  'publishers':publisher_list,
                                                 'authors':author_list
                                                  })


def year_archive(request,year,file_type,user):
    print("-->",year,file_type,user)
    return HttpResponse(year)

def month_archive(request,month,year):
    print("-->",year,month)
    return HttpResponse("%s/%s" %(year,month))
def article_detail(request,year,month,article_id,file_type):
    print("-->",year,month,article_id,file_type)
    return HttpResponse("%s/%s--:[%s.%s]" %(year,month,article_id,file_type))