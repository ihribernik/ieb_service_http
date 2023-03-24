"""
market views
"""
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from market.models import Product
from market.serializers import ProductSerializer

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    """product viewset"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
