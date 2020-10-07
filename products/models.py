from django.db import models
from django.contrib.auth.models import User

from cart.models import Cart

from functools import reduce


class Product(models.Model):
    """Men product items class"""

    SIZE = (("S", "Small"), ("M", "Medium"), ("L", "Large"))
    SEX = (("M", "Male"), ("F", "Female"), ("U", "Unisex"))
    user = models.ForeignKey(User, max_length=100, null=True, on_delete=models.CASCADE)
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

    user = models.ForeignKey(
        User, max_length=100, blank=True, on_delete=models.DO_NOTHING
    )
    subtotal = models.IntegerField(
        default=0.00, verbose_name="Cart items sub-total cost", null=True
    )
    tax = models.IntegerField(default=5.00, verbose_name="Value Added Tax", null=True)
    shipping = models.IntegerField(
        default=0.00, verbose_name="shipping cost", null=True
    )
    total = models.IntegerField(verbose_name="Cart items total cost", null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Calculate total cost before saving data to fields
        """
        if self.subtotal:

            prices_list = []

            for item in Cart.objects.all():
                prices_list.append(item.price)

            items_total_cost = reduce(lambda a, b: a + b, prices_list)
            cumulative_cost = (self.subtotal / 100) * self.tax + items_total_cost

            self.total = cumulative_cost  # real cost

        super().save(*args, **kwargs)  # Real saves method

    class Meta:
        verbose_name = "User shopping order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.product.name
