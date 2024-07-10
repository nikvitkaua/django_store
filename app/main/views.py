from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    context = {
        'title': 'JCY - Home',
        'content': 'Furniture store "JCY"'
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'JCY - About us',
        'content': 'About us',
        'text_on_page': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
    }

    return render(request, 'main/about.html', context)