from django.shortcuts import render,redirect
from crm import models
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from crm import forms
from crm. permissions import  check_permission
# Create your views here.


def dashboard(request):
    return render(request,'crm/dashboard.html')


# @check_permission
def customers(request):
    customer_list = models.Customer.objects.all()
    paginator = Paginator(customer_list,2)
    page = request.GET.get('page')
    try:
        customer_objs = paginator.page(page)
    except PageNotAnInteger:
        customer_objs = paginator.page(1)
    except EmptyPage:
         customer_objs = paginator.page(paginator.num_pages)
    return render(request,'crm/customers.html',{'customer_list':customer_objs})

# @check_permission
def customer_detail(request,customer_id):
    customer_obj = models.Customer.objects.get(id=customer_id)
    if request.method == "POST":
        form = forms.CustomerModelForm(request.POST,instance=customer_obj)
        #print(request.POST)
        if form.is_valid():
            form.save()
            print( 'url:',request.path)
            base_url = "/".join(request.path.split("/")[:-2])
            print( 'url:',base_url)
            return redirect(base_url)
        #else:
    else:
        form = forms.CustomerModelForm(instance=customer_obj)
    return render(request,'crm/customer_detail.html',{'customer_form':form})