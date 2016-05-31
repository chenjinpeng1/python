from django.shortcuts import render
from crm import models
from django.core.paginator import  Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def dashboard(request):
    return render(request,'crm/dashboard.html')
def customer(request):
    customer_list = models.Customer.objects.all()
    paginator = Paginator(customer_list,2) # 每页显示几条,返回一个对象，从对象中获取方法
    page = request.GET.get('page') # 获取客户端传过来的参数，获取page 没有则为none
    print(paginator.num_pages)
    try:
        customer_objs = paginator.page(page) # 如果客户端传过来的参数带页面的页码，则返回该页码的对象给客户端
    except PageNotAnInteger:# 如果客户端传的参数不带页面页码，报异常
        customer_objs = paginator.page(1) #返回第一页
    except EmptyPage: #页码为空或者不存在异常
        customer_objs = paginator.page(paginator.num_pages) # paginator.num_pages返回总页数，在此表示返回尾页
    return render(request,'crm/customer.html',{'customer_list':customer_objs})