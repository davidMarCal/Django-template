from django.shortcuts import render
from django.http import HttpResponse

#----------------
#REQUEST HANLDER
#---------------

# Create your views here.


def say_hello(request):
    x=1
    y=2
    z=x+1
    return render(request,'hello.html',{'name':'User'})