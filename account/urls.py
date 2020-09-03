from django.urls import path, include


urlpatterns = [path("rest-auth/", include("rest_auth.urls"))]
