# # main/models.py
# main/__init__.py
# from .database import Base
# from sqlalchemy import Column, Integer, Float  # Используем Float вместо Decimal
# Base.metadata.create_all(bind=engine)


# from django.db import models
#
# class Product(models.Model):
#     microcategory_id = models.IntegerField()
#     location_id = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)


# class Product(Base):
#     __tablename__ = 'product'
#
#     id = Column(Integer, primary_key=True, index=True)
#     microcategory_id = Column(Integer)
#     location_id = Column(Integer)
#     price = Column(Float)  # Используем Float для хранения цены

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float
from .database import Base
from django.db import models
# from django.db import models



class Product(Base):
    __tablename__ = 'baseline_matrix_1'

    id = Column(Integer, primary_key=True, index=True)
    microcategory_id = Column(Integer)
    location_id = Column(Integer)
    price = Column(Float)  # Используем Float для хранения цены


# class Product_for_admin(models.Model):
#     microcategory_id = models.IntegerField()
#     location_id = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)

# ваш_проект/ваше_приложение/models.py

# from django.db import models
#
# from django.db import models


class Product_1(models.Model):
    microcategory_id = models.IntegerField(primary_key=True)  # Замените на имя столбца первичного ключа в вашей таблице SQLAlchemy
    # microcategory_id = models.IntegerField()
    location_id = models.IntegerField()
    price = models.FloatField()

    class Meta:
        managed = False  # Указывает Django не управлять созданием таблицы
        db_table = 'baseline_matrix_1'  # Указываем имя таблицы SQLAlchemy
