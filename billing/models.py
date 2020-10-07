from django.db import models
from django.contrib.auth.models import User

from country_list import countries_for_language


class Billing(models.Model):
    """Customer billing information class"""

    user = models.OneToOneField(User, unique=True, null=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, null=True)
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Customer billing information"

    def __str__(self):
        return self.email


def countries(countries, COUNTRY_LIST=None):
    all_countries = []

    for key, value in countries:
        all_countries.append((f"{value}-{key}", value))

    COUNTRY_LIST = tuple(all_countries)

    return COUNTRY_LIST


ADDRESS_TYPE = (("billig", "Billing"), ("shipping", "Shipping"))
countries_api = dict(countries_for_language("en")).items()


class Address(models.Model):
    billing = models.OneToOneField(Billing, null=True, on_delete=models.SET_NULL)
    country = models.CharField(
        max_length=50, default="Nigeria", choices=countries(countries_api)
    )  # set list of countries
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPE)
    address_line1 = models.CharField(max_length=250, null=True)
    address_line2 = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = "Customer address information"
        verbose_name_plural = "Addresss"

    def __str__(self):
        return self.billing
