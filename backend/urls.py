from django.contrib import admin
from django.urls import path

from api import urls
from django.conf.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("dj_rest_auth.urls")),
    path("api/registration/", include("dj_rest_auth.registration.urls")),
]
