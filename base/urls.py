from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Render templates endpoint
    path("", include("frontend.urls")),
    # Render API data endpoint
    path("api/v1/", include("products.urls")),
    path("api/v1/carts/", include("cart.urls")),
    # API authentication endpoint
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/rest-auth/", include("accounts.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
