from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context= {
        'title': 'Главная страница',
        'content': "Шмартелье - сделаем одежду из говна"
    }

    return render(request, 'main/index.html', context)

def about(request):
    context= {
        'title': 'О нас',
        'content': "Ононас",
        'text_on_page': "Ебать я ахуенный =))))"
    }

    return render(request, 'main/about.html', context)
