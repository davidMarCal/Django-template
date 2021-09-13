from django.urls import path
from . import views

#URLConf
urlpatterns=[
    #GET
    path('hello/',views.say_hello),
    path('index/',views.show_index),
    path('news-detail/',views.show_news_detail),
    path('user/login/',views.show_login),
    path('user/register/',views.show_register),
    path('user/logOut/',views.logOut),
    
    #POST
    path('user/signUp',views.signUp),
    path('user/signIn',views.signIn),
    path('loadData',views.loadData),
    
]