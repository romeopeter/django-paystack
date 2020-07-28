from rest_framework import serializers
from .models import Product, Order


class ProductSerializer(serializers.ModelSerializer):
    """Products model serializer"""
    class Meta:
        model: Product
        fields: ['id','name','description','image','price']

class OrderSerializer(serializers.ModelSerializer):
    """Products model serializer"""
    class Meta:
        model: Order
        fields: ['id','product', 'created_at']
