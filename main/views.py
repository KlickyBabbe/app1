from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):

    categories= Categories.objects.all()

    context= {
        'title': 'Главная страница',
        'content': "АТЕЛЬЕ",
        'categories': categories
    }

    return render(request, 'main/index.html', context)

def about(request):
    context= {
        'title': 'О нас',
        'content': "О нас",
        'text_on_page': "Самое крутое ателье на планете, делаем лучшую одежду из лучших материалов."
    }

    return render(request, 'main/about.html', context)
