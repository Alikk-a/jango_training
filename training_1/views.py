from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('<h3>Это ми - кошки</h3>')

def home(request):
   return render(request, 'home.html', {'greeting':'Hello, Mike. Hello и ты, Sarah, конечно тоже.'})

def reverse(request):
	user_text = request.GET['piptext']
	words = user_text.split()
	number_of_words = len(words)
	reversed_text = user_text[::-1]
	return render(request, 'reverse.html', {'usertext':user_text,
		'reversedtext':reversed_text, 'number_of_words':number_of_words})