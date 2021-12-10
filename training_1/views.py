from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('<h3>Это ми - кошки</h3>')

def home(request):
   return render(request, 'home.html', {'greeting':'Hello, Mike. Hello и ты, Sarah, конечно тоже.'})
