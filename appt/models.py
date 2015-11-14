from django.db import models

# Create your models here.

class Appointment(models.Model):

	def __str__(self):
		return self.date


	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	date = models.DateTimeField(auto_now=False,auto_now_add=False,null=True)
	doctor = models.CharField(max_length = 50)
	symptoms = models.CharField(max_length = 500)
	available = models.BooleanField()

