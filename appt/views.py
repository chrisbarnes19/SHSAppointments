from django.shortcuts import render
from django.http import HttpResponse

from .models import Appointment

# Create your views here.


def index(request):
	output = "Hello World!"

	return HttpResponse(output)


def monthly_view(request, month):
	p = Appointment.objects.filter_by(date.month = month)


	return HttpResponse('hello')


def date_view(request,date):
	return HttpResponse('hello')


def new_appointment(request,date):
	return HttpResponse('dicks')

def confirmation(request,pk):
	return HttpResponse('fuck you')

def edit(request,pk):
	return HttpResponse('fuck you')



