from django.contrib import admin
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from api.authentication import urls
from django.conf.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(r"api/", include((urls, "authentication"), namespace="authentication")),
]

urlpatterns = format_suffix_patterns(urlpatterns)
