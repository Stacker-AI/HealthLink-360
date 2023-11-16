# from django.shortcuts import render

# from .models import User
# from .serializers import UserSerializer
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView


# class UserView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             User.objects.create_user(**serializer.validated_data)
#             return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
