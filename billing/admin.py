from django.contrib import admin
from .models import Billing, Address

admin.site.register(([Billing, Address]))
