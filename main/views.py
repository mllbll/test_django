# # # main/views.py
from django.shortcuts import render
from .models import Product
from main.database import SessionLocal

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

