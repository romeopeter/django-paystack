from django.db import models
from django.contrib.auth.models import User

from country_list import countries_for_language


# Countries names API
init_country_list = dict(countries_for_language("en"))


def countries_names(countries, all_countries_names=None):
    """
    Tranform countries to tuple of tuples for model field `choices` attribute
    """

    all_countries = []

    for key, value in countries:
        all_countries.append((f"{value}-{key}", value))

    all_countries_names = tuple(all_countries)

    return all_countries_names


# Variable for model field `choices` attribute
ADDRESS_TYPE = (("billig", "Billing"), ("shipping", "Shipping"))
COUNTRY_LIST = countries_names(init_country_list.items())


class Billing(models.Model):
    """Customer billing information class"""

    user = models.OneToOneField(User, unique=True, null=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, null=True)
    timestamp = models.DateField(auto_now_add=True)

    def get_user_email(self, user_email):
        if self.email:
            self.email = user_email

    class Meta:
        verbose_name = "Customer billing information"
        verbose_name_plural = "Billing info"

    def __str__(self):
        return self.email


class Address(models.Model):
    billing = models.OneToOneField(Billing, null=True, on_delete=models.SET_NULL)
    country = models.CharField(max_length=50, default="Nigeria", choices=COUNTRY_LIST)
    state = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPE)
    address_line1 = models.CharField(max_length=250, null=True)
    address_line2 = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = "Customer address information"
        verbose_name_plural = "Address"

    def __str__(self):
        return self.billing
