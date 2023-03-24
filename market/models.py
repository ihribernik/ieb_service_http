"""
market models
"""
from django.db import models


class Product(models.Model):
    """representation of a product"""

    id = models.CharField(primary_key=True, max_length=256)
    buy_price = models.DecimalField(decimal_places=4, max_digits=16)
    sell_price = models.DecimalField(decimal_places=4, max_digits=16)
    description = models.CharField(max_length=256)
