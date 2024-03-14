# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_values, name='input_values'),
]

