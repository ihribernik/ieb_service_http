"""
market views
"""
from rest_framework import permissions, viewsets

from market.models import Product
from market.serializers import ProductSerializer

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    """product viewset"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permision_classes = [permissions.IsAuthenticated]
