from django.contrib import admin
from .models import UserProfile, UserMedicalRecords, Country

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserMedicalRecords)
admin.site.register(Country)
