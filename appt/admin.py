from django.contrib import admin
from .models import Appointment, UserProfile
# Register your models here.
admin.site.register(Appointment)
admin.site.register(UserProfile)