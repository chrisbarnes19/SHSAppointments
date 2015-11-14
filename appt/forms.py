from django import forms
from .models import UserProfile, UserProfileForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfileForm
		fields = ('student_id')