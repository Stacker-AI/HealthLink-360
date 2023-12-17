from rest_framework.serializers import ModelSerializer
from .models import (
    Doctor,
    Patient,
    Appointment,
    Prescription,
    UserProfile,
)


class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"


class PrescriptionSerializer(ModelSerializer):
    class Meta:
        model = Prescription
        fields = "__all__"


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
