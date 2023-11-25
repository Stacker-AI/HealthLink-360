from django.contrib import admin
from django.urls import path, re_path

from api import urls
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("users.urls")),
    path("api/", include("api.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
