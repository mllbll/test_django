# # # main/views.py
# # # from itertools import product
# # #
# # # from django.shortcuts import render
# # # from .models import Product
# #
# #
# # # def get_price(request):
# # #     # obj = Product.objects.all()
# # #     price = None
# # #
# # #     if request.method == 'POST':
# # #         microcategory_id = request.POST['microcategory_id']
# # #         location_id = request.POST['location_id']
# # #
# # #         try:
# # #             product = Product.objects.get(microcategory_id=microcategory_id, location_id=location_id)
# # #             price = product.price
# # #         except Product.DoesNotExist:
# # #             # pass
# # #             price = microcategory_id
# # #
# # #     return render(request, 'get_price.html', {'price': price})
# # #     # return render(request, "get_price.html", {"products": obj})
# #
# # # from django.shortcuts import render
# # # from .models import Product
# # # from django.http import HttpResponse
# # # from main.database import SessionLocal
# # #
# # # def get_price(request):
# # #     session = SessionLocal()
# # #     product = session.query(Product).filter(Product.microcategory_id == 3, Product.location_id == 400).first()
# # #     session.close()
# # #
# # #     if product:
# # #         price = product.price
# # #     else:
# # #         price = None
# # #
# # #     return render(request, 'get_price.html', {'price': price})
# #
# # from django.shortcuts import render
# # from .models import Product
# # from django.http import HttpResponse
# # from main.database import SessionLocal
# # from sqlalchemy.orm import defer
# # from django.shortcuts import render
# # from .models import Product
# # from sqlalchemy.orm import sessionmaker
# # from main.database import engine
# # from django.shortcuts import render
# # from .models import Product
# #
# # # def get_price_1(request):
# # #     price = None
# # #
# # #     if request.method == 'POST':
# # #         microcategory_id = request.POST.get('microcategory_id')
# # #         location_id = request.POST.get('location_id')
# # #
# # #         try:
# # #             product = Product.objects.get(microcategory_id=microcategory_id, location_id=location_id)
# # #             price = product.price
# # #         except Product.DoesNotExist:
# # #             pass
# # #
# # #     return render(request, 'get_price.html', {'price': price})
# #
# #
# # # def get_price(request):
# # #     session = SessionLocal()
# # #     # Измените запрос так, чтобы он выбирал только необходимые столбцы
# # #     product = session.query(Product.microcategory_id, Product.location_id, Product.price).filter(
# # #         Product.microcategory_id == 2, Product.location_id == 400).first()
# # #     session.close()
# # #
# # #     if product:
# # #         price = product.price
# # #     else:
# # #         price = None
# # #
# # #     return render(request, 'get_price.html', {'price': price})
# #
# # # from django.shortcuts import render
# #
# # # def input_values(request):
# # #     if request.method == 'POST':
# # #         # Получаем значения из POST-запроса
# # #         microcategory_id = int(request.POST.get('microcategory_id'))
# # #         location_id = int(request.POST.get('location_id'))
# # #         # Далее вы можете обрабатывать эти значения, например, сохранять их в базу данных или выполнять какие-то другие действия
# # #
# # #         # Возвращаем ответ
# # #         return render(request, 'get_price.html', {'microcategory_id': microcategory_id, 'location_id': location_id})
# # #     else:
# # #         return render(request, 'get_price.html')
# from django.shortcuts import render
#
from django.shortcuts import render
from .models import Product
from main.database import SessionLocal
from django.dispatch import receiver
#
# #
# #
# def input_values(request):
#     if request.method == 'POST':
#         # Получаем значения из POST-запроса
#         microcategory_id = int(request.POST.get('microcategory_id'))
#         location_id = int(request.POST.get('location_id'))
#         # Далее вы можете обрабатывать эти значения, например, сохранять их в базу данных или выполнять какие-то другие действия
#
#         session = SessionLocal()
#         product = session.query(Product.microcategory_id, Product.location_id, Product.price).filter(
#             Product.microcategory_id == microcategory_id, Product.location_id == location_id).first()
#         session.close()
#
#         if product:
#             price = product.price
#         else:
#             price = None
#
#         # Возвращаем ответ
#         return render(request, 'get_price.html',
#                       {'microcategory_id': microcategory_id, 'location_id': location_id, 'price': price})
#     else:
#         return render(request, 'get_price.html')
# #
# # # def input_values(request):
# # #     if request.method == 'POST':
# # #         # Получаем значения из POST-запроса
# # #         microcategory_id = int(request.POST.get('microcategory_id'))
# # #         location_id = int(request.POST.get('location_id'))
# # #         # Далее вы можете обрабатывать эти значения, например, сохранять их в базу данных или выполнять какие-то другие действия
# # #
# # #         # Возвращаем ответ
# # #         return render(request, 'input_values.html', {'microcategory_id': microcategory_id, 'location_id': location_id})
# # #     else:
# # #         return render(request, 'input_values.html')
# # #
# # #
# # # def get_price(request):
# # #     # Здесь вы можете получить доступ к microcategory_id и location_id
# # #     # если они были переданы в предыдущем запросе или сохранены в переменных этого файла
# # #     # Например:
# # #     if 'microcategory_id' in request.POST and 'location_id' in request.POST:
# # #         microcategory_id = int(request.POST.get('microcategory_id'))
# # #         location_id = int(request.POST.get('location_id'))
# # #         session = SessionLocal()
# # #             # Измените запрос так, чтобы он выбирал только необходимые столбцы
# # #         product = session.query(Product.microcategory_id, Product.location_id, Product.price).filter(
# # #             Product.microcategory_id == microcategory_id, Product.location_id == location_id).first()
# # #         session.close()
# # #
# # #         if product:
# # #             price = product.price
# # #         else:
# # #             price = None
# # #
# # #         return render(request, 'get_price.html', {'price': price})
# # # Далее вы можете использовать эти значения как нужно в этом методе
# # # def get_price_1(request):
# # #     price = None
# # #
# # #     if request.method == 'POST':
# # #         microcategory_id = request.POST.get('microcategory_id')
# # #         location_id = request.POST.get('location_id')
# # #
# # #         try:
# # #             product = Product.objects.get(microcategory_id=microcategory_id, location_id=location_id)
# # #             price = product.price
# # #         except Product.DoesNotExist:
# # #             pass
# # #
# # #     return render(request, 'get_price.html', {'price': price})
# # views.py
#
#
# microcategory_id_global = None
# location_id_global = None
#
#
# # @receiver(request_finished)
# def update_global_variables(sender, **kwargs):
#     global microcategory_id_global
#     global location_id_global
#
#     # Обновляем значения глобальных переменных в соответствии с текущими значениями
#     # microcategory_id и location_id из запроса
#     if hasattr(update_global_variables, 'microcategory_id') and hasattr(update_global_variables, 'location_id'):
#         microcategory_id_global = update_global_variables.microcategory_id
#         location_id_global = update_global_variables.location_id
#     else:
#         microcategory_id_global = None
#         location_id_global = None
#
#
# def input_values(request):
#     global microcategory_id_global
#     global location_id_global
#
#     if request.method == 'POST':
#         # Получаем значения из POST-запроса
#         microcategory_id = int(request.POST.get('microcategory_id'))
#         location_id = int(request.POST.get('location_id'))
#         # Далее вы можете обрабатывать эти значения, например, сохранять их в базу данных или выполнять какие-то другие действия
#
#         session = SessionLocal()
#         product = session.query(Product.microcategory_id, Product.location_id, Product.price).filter(
#             Product.microcategory_id == microcategory_id, Product.location_id == location_id).first()
#         session.close()
#
#         if product:
#             price = product.price
#         else:
#             price = None
#
#         # Устанавливаем значения глобальных переменных
#         update_global_variables.microcategory_id = microcategory_id
#         update_global_variables.location_id = location_id
#
#         # Возвращаем ответ
#         return render(request, 'get_price.html',
#                       {'microcategory_id': microcategory_id, 'location_id': location_id, 'price': price})
#     else:
#         return render(request, 'get_price.html')

# views.py
from django.core.cache import cache

def input_values(request):
    if request.method == 'POST':
        # Получаем значения из POST-запроса
        microcategory_id = int(request.POST.get('microcategory_id'))
        location_id = int(request.POST.get('location_id'))
        # Далее вы можете обрабатывать эти значения, например, сохранять их в базу данных или выполнять какие-то другие действия

        session = SessionLocal()
        product = session.query(Product.microcategory_id, Product.location_id, Product.price).filter(
            Product.microcategory_id == microcategory_id, Product.location_id == location_id).first()
        session.close()

        if product:
            price = product.price
        else:
            price = None

        # Кэшируем значения microcategory_id и location_id
        cache.set('microcategory_id', microcategory_id)
        cache.set('location_id', location_id)

        # Возвращаем ответ
        return render(request, 'get_price.html',
                      {'microcategory_id': microcategory_id, 'location_id': location_id, 'price': price})
    else:
        return render(request, 'get_price.html')
