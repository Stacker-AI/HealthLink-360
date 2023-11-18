from django.contrib import admin
from django.urls import path, re_path

from api import urls
from django.conf.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path("^auth/", include("djoser.urls")),
    re_path("^auth/", include("djoser.urls.jwt")),
]
