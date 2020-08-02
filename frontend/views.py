from django.shortcuts import render

from products.models import Product

# Create your views here.


def index(request):
    context = {"title": "Django Paystack"}
    return render(request, "frontend/index.html", context)
