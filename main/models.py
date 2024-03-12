# main/models.py

from django.db import models

class Product(models.Model):
    microcategory_id = models.IntegerField()
    location_id = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
