from django import forms
from .models import UserProfile, Appointment
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('student_id',)


class AppointmentForm(forms.Form):
	symptoms = forms.CharField(max_length = 500)
	