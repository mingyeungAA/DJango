"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#같은 폴더에 있는 views
from . import views

urlpatterns = [ 
    path('admin/', admin.site.urls),
    # '' : localhost:8000
    path('', views.index),
    #hello01로 넘어온것은 여기서 다 처리한다.
    path('hello01/', include('hello01.urls')),
    #hello02>urls.py에서 넘어온 값을 여기서 받아서 다시 hello02.urls.py로 넘김
    path('hello02/', include('hello02.urls')),
]
