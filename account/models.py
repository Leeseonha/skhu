from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    grade = models.IntegerField(null=True)
    major = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    student_id = models.CharField(max_length=20)
    pass_or_not = models.BooleanField(null=True, blank=True)