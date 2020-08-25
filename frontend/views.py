from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie


from products.models import Product

# Create your views here.


@ensure_csrf_cookie
def index(request):
    context = {"title": "Django Paystack"}
    return render(request, "frontend/index.html", context)
