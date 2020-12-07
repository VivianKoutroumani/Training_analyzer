from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# This file creates several user forms and defines update settings.


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # password2 is used for password confirmation.


# Creates the form we use to update the "User" model.
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()  # True by default.

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):  # Allows the user to update their profile after having made it.
    class Meta:
        model = Profile
        fields = ['image']
