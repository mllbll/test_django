# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_values, name='input_values'),
]
# from django.urls import path
# from django.contrib import admin
# from .views import product_list
#
# urlpatterns = [
#     path('', product_list, name='home'),  # Пустой URL
#     path('admin/', admin.site.urls),      # Используем admin из django.contrib
#     path('products/', product_list, name='product_list'),
#     # Добавьте другие маршруты URL по мере необходимости
# ]
