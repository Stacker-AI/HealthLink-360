from rest_framework.serializers import ModelSerializer
from .models import UserMedicalRecords, UserProfile


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class UserMedicalRecordsSerializer(ModelSerializer):
    class Meta:
        model = UserMedicalRecords
        fields = "__all__"
