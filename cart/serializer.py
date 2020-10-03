from rest_framework import serializers

from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        models = Cart
        fields = "__all__"
