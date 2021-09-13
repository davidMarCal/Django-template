from playground.models import Person
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

#----------------
#REQUEST HANLDER
#---------------

#
# Views 
#

def say_hello(request):
    x=1
    y=2
    z=x+1
    return render(request,'hello.html',{'name':'User'})

def show_index(request):
    return render(request,'index.html')

def show_login(request):
    return render(request,'user/login.html') 

def show_register(request):
    return render(request,'user/register.html') 

@login_required(login_url='/playground/user/login/')
def show_news_detail(request):

    try:
        person=Person.objects.get_person(request.user)
        return render(request,'news-detail.html',{'person':person})
    except:
        print("No user data registered")
        return render(request,'news-detail.html',{'person':""})

@login_required(login_url='/playground/user/login/')
def loadData(request):
    first_name=(str(request.POST["name"]))
    last_name=(str(request.POST["last_name"]))
    try:
        person=Person.objects.get_person(user=request.user)
    except:
        person=""
    if(person):
        person=Person.objects.update_person(user=request.user,first_name=first_name,last_name=last_name)
    else:
        person=Person.objects.create_person(user=request.user,first_name=first_name,last_name=last_name)
        person.save()
    return redirect('news-detail/')
#
# Users 
#

def signUp(request):
    username=(str(request.POST["username"]))
    email=(str(request.POST["email"]))
    password=(str(request.POST["password"]))
    confirm_password=(str(request.POST["rpassword"]))
    if password != confirm_password:
        messages.error(request,' Passwords mismatch')
        return render(request,'user/register.html') 
    else:
        user = User.objects.create_user(username,email,password)
        user.save()
        return render(request,'user/login.html')

def signIn(request):
    username=(str(request.POST["username"]))
    password=(str(request.POST["password"]))

    user = authenticate(username=username, password=password)
    if user is not None:
        # A backend authenticated the credentials
        login(request, user)
        return redirect('/playground/news-detail',user)
    else:
        # No backend authenticated the credentials
        messages.error(request,' Username or password not correct')
        return render(request,'user/login.html') 

def changePass(request):
    username=(str(request.POST["username"]))
    password=(str(request.POST["password"]))
    u = User.objects.get(username=username)
    u.set_password(password)
    u.save()
    messages.error(request,' Username or password not correct')
    return render(request,'user/login.html')

def logOut(request):
    logout(request)
    return redirect('/playground/index')