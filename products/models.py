from django.db import models


class Product(models.Model):
    """Men product items class"""

    CHOICE = (("M", "Male"), ("F", "Female"))
    SIZE = (("S", "Small"), ("M", "Medium"), ("L", "Large"))

    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to="uploads/%Y/%m/%d", null=True, blank=True)
    size = models.CharField(max_length=1, null=True, choices=SIZE)
    sex = models.CharField(max_length=1, null=True, choices=CHOICE)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    """Order for product item"""

    product = models.ForeignKey(
        Product, max_length=200, blank=True, on_delete=models.DO_NOTHING
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
