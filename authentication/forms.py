from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, UserFollowersModel

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['is_active',]

class UserProfileFirstForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

class FollowUserForm(forms.ModelForm):
    class Meta:
        model = UserFollowersModel
        fields = '__all__'