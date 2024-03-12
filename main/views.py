# main/views.py

from django.shortcuts import render
from .models import Product


def get_price(request):
    price = None

    if request.method == 'POST':
        microcategory_id = request.POST.get('microcategory_id')
        location_id = request.POST.get('location_id')

        try:
            product = Product.objects.get(microcategory_id=microcategory_id, location_id=location_id)
            price = product.price
        except Product.DoesNotExist:
            pass

    return render(request, 'get_price.html', {'price': price})
