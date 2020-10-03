from django.db import models
from django.db.models.signals import pre_save
from django.db.models.signals import m2m_changed

from django.contrib.auth.models import User

from products.models import Product

# Create your models here.
class Cart(models.Model):
    """Cart class model"""

    user = models.ForeignKey(
        User, verbose_name="cart owner", on_delete=models.DO_NOTHING
    )
    product = models.ManyToManyField(Product)
    product_image_url = models.CharField(max_length=200, null=True)
    product_subtotal = models.DecimalField(
        default=0.00, max_digits=100, decimal_places=2, null=True
    )
    product_total = models.DecimalField(
        default=0.00, max_digits=100, decimal_places=2, null=True
    )
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name


def prouduct_m2m_change_reciever(sender, action, instance, *args, **kwargs):
    if action == "post_add" or action == "post_removed" or action == "post.clear":
        product_fields = instance.product.all()

        sub_price = 0
        image_url = ""

        for field in product_fields:
            sub_price += field.price
            image_url += field.product_image_url

        instance.product_subtotal = sub_price
        instance.product_image_url = image_url
        instance.save()


m2m_changed.connect(prouduct_m2m_change_reciever, sender=Cart)


def cart_product_total_reciever(sender, instance, *args, **kwargs):
    if instance.product_subtotal > 0:
        calculate_for_tax = float(instance.product_subtotal) * float(1.8)
        instance.product_total = calculate_for_tax
    instance.product_total = 0.00


pre_save.connect(cart_product_total_reciever, sender=Cart)
