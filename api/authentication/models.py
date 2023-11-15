from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=50, blank=False, unique=True)
    password = models.CharField(max_length=50, blank=False)
    username = models.CharField(
        max_length=50, blank=False, unique=True, default="username"
    )
