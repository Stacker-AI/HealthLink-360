from django.urls import path
from api.views import (
    DoctorView,
    PatientView,
    AppointmentView,
    PrescriptionView,
    UserProfileView,
)
from . import views


urlpatterns = [
    path("profile/", UserProfileView.as_view()),
    path("doctors/", DoctorView.as_view()),
    path("patients/", PatientView.as_view()),
    path("appointments/", AppointmentView.as_view()),
    path("prescriptions/", PrescriptionView.as_view()),
]
