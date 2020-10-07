from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1><a href="/hello01">Hello, Django!</a></h1>')