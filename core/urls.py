from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('menu/', menu, name='menu'),
    path('about/', about, name='about'),
]
