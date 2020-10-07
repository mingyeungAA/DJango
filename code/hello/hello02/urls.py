from django.urls import path
from . import views


urlpatterns=[
    #hello02로 요청이 들어오면, views.hello로 연결해줄거여ㅑ
    #그럼 hello>hello의 urls.py로가서 hello02로 보낸다.
    path('', views.hello, name='index'),
    path('var01', views.variable01),
    path('var02', views.variable02),
    path('for', views.forLoop),
    path('if01', views.if01),
    path('if02', views.if02),
    path('href', views.href)
]