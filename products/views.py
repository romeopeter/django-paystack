from django.shortcuts import render

from rest_framework import viewsets, generics
from rest_framework.response import Response

from .models import Product
from .serializer import ProductSerializer


class ProductsViewSet(viewsets.ViewSet):
    """List products viewset"""

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
