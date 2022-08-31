from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('location/', location, name='location'),
    path('rest_zone/', rest_zone, name='rest_zone'),
    path('booking_page/', booking_page, name='booking_page'),
]
