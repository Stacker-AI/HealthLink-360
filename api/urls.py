from django.urls import path
from api.views import UserProfileView, UserMedicalRecordsView
from . import views


urlpatterns = [
    path("profile/", UserProfileView.as_view()),
    path("records/", UserMedicalRecordsView.as_view()),
]
