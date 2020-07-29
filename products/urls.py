from django.urls import path

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("products", views.ProductsViewSet, basename="products")

urlpatterns = router.urls
