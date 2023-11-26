from .models import UserMedicalRecords, UserProfile
from .serializers import UserMedicalRecordsSerializer, UserProfileSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser


class UserProfileView(APIView):
    def get(self, request, format=None):
        user = request.user
        try:
            user_profile = UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            message = {"message": "No profile found"}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data.copy()
        data["user"] = request.user.id
        serializer = UserProfileSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserMedicalRecordsView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, format=None):
        user = request.user
        try:
            user_medical_records = UserMedicalRecords.objects.get(user=user)
        except UserMedicalRecords.DoesNotExist:
            message = {"message": "No medical records found"}
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        serializer = UserMedicalRecordsSerializer(user_medical_records)
        return Response(serializer.data)

    def post(self, request, format=None):
        file_obj = request.FILES.get("files")
        if not file_obj:
            message = {"message": "No file found"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        file_type = request.data.get("file_type")
        if not file_type:
            message = {"message": "No file type found"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        data = {
            "user": request.user.id,
            "files": file_obj,
            "file_type": file_type,
        }
        serializer = UserMedicalRecordsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def patch(self, request, pk, format=None):
    #     file_obj = request.FILES.get("files")
    #     if not file_obj:
    #         message = {"message": "No file found"}
    #         return Response(message, status=status.HTTP_400_BAD_REQUEST)

    #     file_type = request.data.get("file_type")
    #     if not file_type:
    #         message = {"message": "No file type found"}
    #         return Response(message, status=status.HTTP_400_BAD_REQUEST)

    #     data = {
    #         "user": request.user.id,
    #         "files": file_obj,
    #         "file_type": file_type,
    #     }
    #     try:
    #         user_medical_records = UserMedicalRecords.objects.get(pk=pk)
    #     except UserMedicalRecords.DoesNotExist:
    #         message = {"message": "No medical records found"}
    #         return Response(message, status=status.HTTP_404_NOT_FOUND)

    #     serializer = UserMedicalRecordsSerializer(user_medical_records, data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)
