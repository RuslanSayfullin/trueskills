from django.http import HttpResponse
from django.shortcuts import render

menu = [{'title': "Главная страница", 'url_name': 'index'},
        {'title': "Страница с результатами поиска локаций", 'url_name': 'location'},
        {'title': "Страница выбора конкретной зоны из свободных в локации", 'url_name': 'rest_zone'},
        {'title': "Страница бронирования", 'url_name': 'booking_page'}
]


def index(request):
    context = {
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'trueskills/index.html', context=context)


def location(request):
    context = {
        'menu': menu,
        'title': 'Страница с результатами поиска локаций'
    }
    return render(request, 'trueskills/location.html', context=context)


def rest_zone(request):
    context = {
        'menu': menu,
        'title': 'Страница с результатами поиска локаций'
    }
    return render(request, 'trueskills/rest_zone.html', context=context)


def booking_page(request):
    context = {
        'menu': menu,
        'title': 'Страница с результатами поиска локаций'
    }
    return render(request, 'trueskills/booking_page.html', context=context)
