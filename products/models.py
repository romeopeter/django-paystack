from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """Men product items class"""

    SIZE = (("S", "Small"), ("M", "Medium"), ("L", "Large"))
    SEX = (("M", "Male"), ("F", "Female"), ("U", "Unisex"))
    user = models.ForeignKey(User, max_length=100, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to="uploads/%Y/%m/%d", null=True, blank=True)
    sex = models.CharField(max_length=1, null=True, choices=SEX)
    size = models.CharField(max_length=1, null=True, choices=SIZE)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    """Order for product item"""

    product = models.ForeignKey(
        Product, max_length=100, blank=True, on_delete=models.DO_NOTHING
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
