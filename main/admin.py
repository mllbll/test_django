from django.contrib import admin
from .models import Product_1
from main.views import input_values
from django.core.cache import cache


class ProductAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        microcategory_id = cache.get('microcategory_id')
        location_id = cache.get('location_id')
        if microcategory_id is None or location_id is None:
            # Если значения не найдены в кэше, вернем пустой QuerySet
            return Product_1.objects.none()
        return super().get_queryset(request).filter(microcategory_id=microcategory_id,
                                                    location_id=location_id)


admin.site.register(Product_1, ProductAdmin)
