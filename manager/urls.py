from .views import manager
from django.urls import path
urlpatterns = [
    path('', manager, name='manager'),
]