from django.contrib import admin
from django.urls import path, re_path

from api import urls
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("api.urls")),
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("users.urls")),
]
