from rest_framework.serializers import ModelSerializer
from .models import UserMedicalRecords, UserProfile, Country

class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"  # all fields

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class UserMedicalRecordsSerializer(ModelSerializer):
    class Meta:
        model = UserMedicalRecords
        fields = "__all__"
