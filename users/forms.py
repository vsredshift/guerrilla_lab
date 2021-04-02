# Extend built-in django forms with customisable forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile  # to update profile picture

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()      #  required=True by default

    class Meta:     # specify interaction model. Nested namespace
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# update user
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# image is in Profile model
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']