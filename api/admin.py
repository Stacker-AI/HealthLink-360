from django.contrib import admin
from .models import UserProfile, UserMedicalRecords

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserMedicalRecords)
