from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

#----------------
#REQUEST HANLDER
#---------------

# Create your views here.
def say_hello(request):
    x=1
    y=2
    z=x+1
    return render(request,'hello.html',{'name':'User'})

def show_index(request):
    return render(request,'index.html')

def show_news_detail(request):
    return render(request,'news-detail.html')

def show_login(request):
    return render(request,'user/login.html') 

def show_register(request):
    return render(request,'user/register.html') 