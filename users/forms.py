# Extend built-in django forms with customisable forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile  # to update profile picture

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()      #  required=True by default
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:     # specify interaction model. Nested namespace
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


# update user
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

# image is in Profile model
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']