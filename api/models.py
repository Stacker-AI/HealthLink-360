from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL



class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)

    # personal info
    location = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)

    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    contact_number = models.IntegerField(blank=True, null=True)
    emergency_contact_number = models.IntegerField(blank=True, null=True)

    gender = models.CharField(
        choices=(("male", "Male"), ("female", "Female")), max_length=10
    )
    blood_group = models.CharField(
        (
            ("A+", "A+"),
            ("A-", "A-"),
            ("B+", "B+"),
            ("B-", "B-"),
            ("AB+", "AB+"),
            ("AB-", "AB-"),
            ("O+", "O+"),
            ("O-", "O-"),
        ),
        max_length=10,
    )
    martial_status = models.CharField(
        models.CharField(("single", "Single"), ("married", "Married")), max_length=10
    )

    # medical info
    allergies = models.JSONField(blank=True, null=True, default=dict)
    current_medications = models.JSONField(blank=True, null=True, default=dict)
    past_medications = models.JSONField(blank=True, null=True, default=dict)
    chronic_diseases = models.JSONField(blank=True, null=True, default=dict)
    injuries = models.JSONField(blank=True, null=True, default=dict)
    surgeries = models.JSONField(blank=True, null=True, default=dict)

    # lifestyle info
    smoking = models.BooleanField(default=False)
    alcohol = models.BooleanField(default=False)
    activity_level = models.CharField(
        choices=(("low", "Low"), ("high", "High")), max_length=10
    )
    food_habits = models.CharField(
        models.CharField(("veg", "Vegetarian"), ("non-veg", "Non-Vegetarian")),
        max_length=10,
    )
    sleep_habits = models.CharField(
        choices=(("early", "Early Bird"), ("night", "Night Owl")), max_length=10
    )
    occupation = models.CharField(max_length=100, blank=True, null=True)


class UserMedicalRecords(models.Model):
    user = models.ForeignKey(
        User, related_name="medical_records", on_delete=models.CASCADE
    )
    # medical files

    FILE_TYPES = (
        ("prescriptions", "Prescriptions"),
        ("reports", "Reports"),
        ("test_results", "Test Results"),
        ("invoices", "Invoices"),
    )

    files = models.FileField(upload_to="medical_records/")
    file_type = models.CharField(max_length=20, choices=FILE_TYPES)

    def __str__(self):
        return self.file_type
