from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#Creating user forms & define updating settings

class UserRegisterForm(UserCreationForm): 
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']#password2 is for password confirmation

class UserUpdateForm(forms.ModelForm):   # form to update user model
	email = forms.EmailField()#true by default

	class Meta:
			model = User
			fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm): #allow updating the user's profile
		class Meta:
				model = Profile
				fields = ['image']