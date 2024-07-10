from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    context = {
        'title': 'Home',
        'content': 'Home page for store'
    }

    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('About page')