from django.urls import path

from .views import AddItemToCart

app_name = "cart"
urlpatterns = [path("", AddItemToCart.as_view(), name="cart")]
