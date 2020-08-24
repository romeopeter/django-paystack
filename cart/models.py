from django.db import models
from django.db.models.signals import pre_save, m2m_changed

from products.models import Product

# Create your models here.
class Cart(models.Model):
    """Cart class model"""

    product = models.ManyToManyField(Product)
    product_image_url = models.CharField(max_length=200, null=True)
    product_subtotal = models.DecimalField(
        default=0.00, max_digits=100, decimal_places=2
    )
    product_total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
