# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=50)
#     full_name = models.CharField(max_length=250, null=True)
#     email = models.EmailField()
#     is_stuff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.username