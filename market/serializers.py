"""market serializers"""
from rest_framework import serializers, permissions
from market.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """product serializer"""

    class Meta:
        """metaclass for product serializer"""

        model = Product
        fields = ["id", "buy_price", "sell_price", "description"]
        permission_classes = [permissions.IsAuthenticated]
