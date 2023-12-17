from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


# PatientModel
class Patient(models.Model):
    user = models.OneToOneField(User, related_name="patient", on_delete=models.CASCADE)

    # personal info
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    martial_choices = (("single", "Single"), ("married", "Married"))
    martial_status = models.CharField(choices=martial_choices, max_length=10)

    # medical info
    allergies = models.JSONField(blank=True, null=True, default=dict)
    current_medications = models.JSONField(blank=True, null=True, default=dict)
    past_medications = models.JSONField(blank=True, null=True, default=dict)
    chronic_diseases = models.JSONField(blank=True, null=True, default=dict)
    injuries = models.JSONField(blank=True, null=True, default=dict)
    surgeries = models.JSONField(blank=True, null=True, default=dict)
    systolic_bp = models.PositiveIntegerField(default=120, blank=True, null=True)
    diastolic_bp = models.PositiveIntegerField(default=80, blank=True, null=True)
    glucose_upper = models.DecimalField(
        max_digits=5, decimal_places=2, default=100, blank=True, null=True
    )
    glucose_lower = models.DecimalField(
        max_digits=5, decimal_places=2, default=70, blank=True, null=True
    )
    blood_count = models.IntegerField(default=9456, blank=True, null=True)

    def __str__(self):
        return self.user.email


# DoctorModel
class Doctor(models.Model):
    user = models.OneToOneField(User, related_name="doctor", on_delete=models.CASCADE)

    # personal info
    days_choices = (
        ("mon", "Monday"),
        ("tue", "Tuesday"),
        ("wed", "Wednesday"),
        ("thu", "Thursday"),
        ("fri", "Friday"),
        ("sat", "Saturday"),
        ("sun", "Sunday"),
    )
    days = models.CharField(choices=days_choices, max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()
    fees = models.IntegerField(blank=True, null=True)
    speciality = models.CharField(max_length=100, blank=True, null=True)
    medical_degree = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.email


# AppointmentModel
class Appointment(models.Model):
    patient = models.ForeignKey(
        Patient, related_name="appointments", on_delete=models.CASCADE
    )
    doctor = models.ForeignKey(
        Doctor, related_name="appointments", on_delete=models.CASCADE
    )

    date = models.DateTimeField(auto_now_add=True)
    time = models.TimeField()
    symptoms = models.JSONField(default=dict)
    notes = models.TextField(blank=True, null=True)
    report = models.FileField(upload_to="", blank=True, null=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.patient.user.email


class Prescription(models.Model):
    patient = models.ForeignKey(
        Patient, related_name="prescriptions", on_delete=models.CASCADE
    )
    doctor = models.ForeignKey(
        Doctor, related_name="prescriptions", on_delete=models.CASCADE
    )
    date = models.DateTimeField(auto_now_add=True)
    symptoms = models.JSONField(default=dict)
    disease = models.CharField(max_length=100)
    medication = models.JSONField(default=dict)
    tests = models.JSONField(default=dict)
    follow_up = models.JSONField(default=dict)
    remarks = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.patient.user.email


# UserProfileModel
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)

    # personal info
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)

    number = models.IntegerField(blank=True, null=True)
    emergency_no = models.IntegerField(blank=True, null=True)
    gender_choices = (("male", "Male"), ("female", "Female"))
    gender = models.CharField(choices=gender_choices, max_length=10)

    def __str__(self):
        return self.user.email
