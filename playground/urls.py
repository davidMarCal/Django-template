from django.urls import path
from . import views

#URLConf
urlpatterns=[
    path('hello/',views.say_hello),
    path('index/',views.show_index),
    path('news-detail/',views.show_news_detail)
]