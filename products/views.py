from rest_framework import generics, permissions

from .models import Product
from .serializer import ProductSerializer


class ProductListView(generics.ListAPIView):
    """List products viewset"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
