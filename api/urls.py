from django.urls import path
from api.views import UserProfileView, UserMedicalRecordsView, CountryView
from . import views


urlpatterns = [
    path("profile/", UserProfileView.as_view()),
    path("records/", UserMedicalRecordsView.as_view()),
    path("countries/", CountryView.as_view()),
]
