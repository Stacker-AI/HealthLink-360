# Generated by Django 4.2.7 on 2023-12-28 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(choices=[('mon', 'Monday'), ('tue', 'Tuesday'), ('wed', 'Wednesday'), ('thu', 'Thursday'), ('fri', 'Friday'), ('sat', 'Saturday'), ('sun', 'Sunday')], max_length=10)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('fees', models.IntegerField(blank=True, null=True)),
                ('speciality', models.CharField(blank=True, max_length=100, null=True)),
                ('medical_degree', models.CharField(blank=True, max_length=100, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('martial_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married')], max_length=10)),
                ('allergies', models.JSONField(blank=True, default=dict, null=True)),
                ('current_medications', models.JSONField(blank=True, default=dict, null=True)),
                ('past_medications', models.JSONField(blank=True, default=dict, null=True)),
                ('chronic_diseases', models.JSONField(blank=True, default=dict, null=True)),
                ('injuries', models.JSONField(blank=True, default=dict, null=True)),
                ('surgeries', models.JSONField(blank=True, default=dict, null=True)),
                ('systolic_bp', models.PositiveIntegerField(blank=True, default=120, null=True)),
                ('diastolic_bp', models.PositiveIntegerField(blank=True, default=80, null=True)),
                ('glucose_upper', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5, null=True)),
                ('glucose_lower', models.DecimalField(blank=True, decimal_places=2, default=70, max_digits=5, null=True)),
                ('blood_count', models.IntegerField(blank=True, default=9456, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('emergency_no', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('symptoms', models.JSONField(default=dict)),
                ('disease', models.CharField(max_length=100)),
                ('medication', models.JSONField(default=dict)),
                ('tests', models.JSONField(default=dict)),
                ('follow_up', models.JSONField(default=dict)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescriptions', to='api.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescriptions', to='api.patient')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('time', models.TimeField()),
                ('symptoms', models.JSONField(default=dict)),
                ('notes', models.TextField(blank=True, null=True)),
                ('report', models.FileField(blank=True, null=True, upload_to='')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='api.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='api.patient')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]