from django.urls import path
from . import views

urlpatterns = [
    path(r"register/", views.UserView.as_view()),
]
