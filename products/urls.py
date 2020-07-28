from django.urls import path

from .views import ProductsListView
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('products', views.ProductsListView, basename='products')

urlpatterns = router.urls
