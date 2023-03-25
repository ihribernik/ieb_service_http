from django.core.management.base import BaseCommand
from django.utils.log import logging
from market.models import Product
from market.factories import ProductFactory


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        if Product.objects.count() == 0:
            logging.info("creating some user...")
            for num in range(20):
                new_product = ProductFactory()
                result = Product.objects.create(
                    id=new_product.id,
                    buy_price=new_product.buy_price,
                    sell_price=new_product.sell_price,
                    description=new_product.description,
                )
                print(f"Successfully created row {num}  id {result}")
        else:
            products = Product.objects.all()
            for product in products:
                new_product = ProductFactory()
                product.buy_price = new_product.buy_price
                product.sell_price = new_product.sell_price
                product.save()
                print(f"Successfully updated row {product}")
