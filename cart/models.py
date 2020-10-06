from django.db import models
from django.db.models.signals import post_save

from django.contrib.auth.models import User

from products.models import Product

# Create your models here.
class Cart(models.Model):
    """Cart model table"""

    user = models.ForeignKey(
        User, null=True, verbose_name="cart owner", on_delete=models.DO_NOTHING
    )
    name = models.CharField(max_length=100, null=True)
    image_url = models.CharField(max_length=200, null=True)
    sex = models.CharField(max_length=10, null=True)
    size = models.CharField(max_length=10, null=True)
    subtotal = models.DecimalField(
        default=0.00, max_digits=100, decimal_places=2, null=True
    )
    total = models.DecimalField(
        default=0.00, max_digits=100, decimal_places=2, null=True
    )
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.subtotal > 0:
            calculate_for_tax = float(self.subtotal) * float(1.8)
            self.total = calculate_for_tax

            super().save(*args, **kwargs)

    def __str__(self):
        return self.name
