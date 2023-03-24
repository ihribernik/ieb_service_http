"""market serializers"""
from rest_framework import serializers
from market.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """product serializer"""

    class Meta:
        """metaclass for product serializer"""

        model = Product
        fields = ["id", "buy_price", "sell_price", "description"]
