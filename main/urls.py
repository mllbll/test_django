# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_price, name='get_price'),
]
