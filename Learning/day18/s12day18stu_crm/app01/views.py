from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.

@login_required
def index(request):
    return render(request,'index.html')


def acc_login(request):
    if request.method == 'POST':
        print(request.POST)
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is not None:
            #pass authentication
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            login_err = "Wrong username or password!"
            return render(request,'login.html',{'login_err':login_err})
    return render(request,'login.html')

def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/')