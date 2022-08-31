from django.http import HttpResponse
from django.shortcuts import render

menu = [{'title': "Главная страница", 'url_name': 'index'},
        {'title': "Акции", 'url_name': 'location'},
        {'title': "Поиск", 'url_name': 'rest_zone'},
        {'title': "Управление бронированием", 'url_name': 'booking_page'}
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
    return render(request, 'trueskills/search.html', context=context)


def rest_zone(request):
    context = {
        'menu': menu,
        'title': 'Страница с результатами поиска локаций'
    }
    return render(request, 'trueskills/seat.html', context=context)


def booking_page(request):
    context = {
        'menu': menu,
        'title': 'Страница с результатами поиска локаций'
    }
    return render(request, 'trueskills/booking.html', context=context)
