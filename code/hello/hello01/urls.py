from django.urls import path
from . import views


urlpatterns =[
    #hello01로 들어오면,
    path('',views.index),
    #url이 test로 들어오면, views의 test가 호출됨
    path('test', views.test)
]