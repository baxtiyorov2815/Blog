from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     GENDERS = (
#         'male': 'Male',
#         'female': 'Female',
#         'other': 'Other'
#     )
#     username = models.CharField(max_length=50)
#     full_name = models.CharField(max_length=250, null=True)
#     email = models.EmailField()
#     addres = models.TextField(null=True)
#     gender = models.Choices(value=GENDERS)
#     is_stuff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(
        to=User,
        verbose_name="user profile",
        on_delete=models.CASCADE
    )
    followers = models.ManyToManyField(
        to=User,
        related_name="followed_profiles",
        blank=True
    )
    full_name = models.CharField(max_length=250, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    pro_picture = models.ImageField(upload_to="users/", null=True, blank=True)
    phone_number = models.CharField(
        max_length=25,
        null=True,
        blank=True,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Enter a valid phone number.")]
    )
    mobile_number = models.CharField(
        max_length=25,
        null=True,
        blank=True,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Enter a valid mobile number.")]
    )
    web_url = models.URLField(max_length=200, null=True, blank=True)
    github_url = models.URLField(max_length=200, null=True, blank=True)
    twitter_url = models.URLField(max_length=200, null=True, blank=True)
    insta_url = models.URLField(max_length=200, null=True, blank=True)
    facebook_url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username if self.user else "Anonymous User"

    
class UserFollowersModel(models.Model):
    user = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)