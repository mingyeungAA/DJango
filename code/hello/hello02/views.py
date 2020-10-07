from django.shortcuts import render

# Create your views here.
def hello(request):
    #요청받은 것을 hello02.html로 넘겨줄건데, name이랑 'DJango' 데이터를 넘겨줄겨
    return render(request, 'hello02.html', {'name':'Django'})


def variable01(request):
    lst = ['Python','Django','Templates']
    #lst를 list라는 이름으로 보낼거야
    return render(request, 'variable01.html', {'list':lst})



def variable02(request):
    dct = {'class' : 'qclass', 'name' : 'ming'}
    return render(request, 'variable02.html', {'dct': dct})


def forLoop(request):
    return render(request, 'for.html', {'number' : range(1,10)})



def if01(request):
    return render(request, 'if01.html', {'user' : {'id' : 'qclass', 'name' : 'ming'}})


def if02(request):
    return render(request, 'if02.html', {'role':'manager'})



def href(request):
    return render(request, 'href.html')

