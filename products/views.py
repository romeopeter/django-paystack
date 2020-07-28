from django.shortcuts import render

from .models import Product

from rest_framework import viewsets, generics
from rest_framework.response import Response

from .serializer import ProductSerializer

class ProductsListView(viewsets.ViewSet):
    """List products viewset"""
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

