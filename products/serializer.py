from rest_framework import serializers
from .models import Product, Order


class ProductSerializer(serializers.ModelSerializer):
    """Products model serializer"""

    image = serializers.SerializerMethodField("get_image_url")

    class Meta:
        model = Product
        fields = "__all__"

    def get_image_url(self, obj):
        # request = self.context.get("request")
        # request.build_absolute_uri(obj.image.url)
        return obj.image.url


class OrderSerializer(serializers.ModelSerializer):
    """Order model serializer"""

    class Meta:
        model = Order
        fields = "__all__"
