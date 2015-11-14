from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Appointment(models.Model):

	def __str__(self):
		return self.name


	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	date = models.DateTimeField(auto_now=False,auto_now_add=False,null=True)
	doctor = models.CharField(max_length = 50)
	symptoms = models.CharField(max_length = 500)
	available = models.BooleanField()

class UserProfile(models.Model):
	# links user profile to User model instance
	user = models.OneToOneField(User)

	# additional attributes
	student_id = models.IntegerField(null = True)

	# override __unicode__()
	def __unicode__(self):
		return self.user.username