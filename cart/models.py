from django.db import models
from django.db.models.signals import post_save

from django.contrib.auth.models import User

# Create your models here.
class Cart(models.Model):
    """Cart model table"""

    user = models.ForeignKey(
        User, verbose_name="cart owner", null=True, on_delete=models.DO_NOTHING
    )
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, blank=True)
    image_url = models.CharField(max_length=200, null=True)
    sex = models.CharField(max_length=10, null=True)
    size = models.CharField(max_length=10, null=True)
    price = models.FloatField(default=0.00, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
