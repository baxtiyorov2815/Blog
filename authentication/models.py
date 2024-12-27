from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class CustomUser(AbstractBaseUser, PermissionsMixin):
    GENDERS = (
        'male': 'Male',
        'female': 'Female',
        'other': 'Other'
    )
    username = models.CharField(max_length=50)
    full_name = models.CharField(max_length=250, null=True)
    email = models.EmailField()
    addres = models.TextField(null=True)
    gender = models.Choices(value=GENDERS)
    is_stuff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username