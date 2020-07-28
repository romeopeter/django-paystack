from django.db import models

class Product(models.Model):
    """Product items"""
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    """Order for product item"""
    product = models.ForeignKey(Product, max_length=200, blank=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
