from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Appointment, UserProfile
from .forms import UserForm, UserProfileForm, AppointmentForm

# Create your views here.


def index(request):
	output = "Hello World!"

	return HttpResponse(output)

@login_required
def monthly_view(request, month):
	
	return HttpResponse('hello')


@login_required
def date_view(request,day,month,year):
	
	appointments = get_list_or_404(Appointment, date >= datetime.datetime(year = year, month = month, day = day), date <= datetime.datetime(year = year, month = month, day = day + 1), available = True)

	return render_to_response('appt/dateview.html',{'appointments':appointments,},context)

@login_required
def new_appointment(request,pk):

	context = RequestContext(request)

	my_appointment = get_object_or_404(Appointment, pk = pk)
	my_userprofile = get_object_or_404(UserProfile, pk = request.user.pk)


	if request.method == 'POST':

		appointment_form = AppointmentForm(data=request.POST)

		if appointment_form.is_valid():

			my_appointment.user_profile = my_userprofile
			my_appointment.symptoms = appointment_form.cleaned_data['symptoms']
			my_appointment.available = False
			my_appointment.save()

		else:
			print appointment_form.errors


	else:
		appointment_form = AppointmentForm()


	return render_to_response('appt/newappointment.html',{'my_appointment': my_appointment, 'appointment_form':appointment_form}, context)

@login_required
def confirmation(request,pk):

	context = RequestContext(request)

	my_appointment = get_object_or_404(Appointment, pk = pk)
	my_userprofile = get_object_or_404(UserProfile, pk = request.user.pk)


	return render_to_response('appt/confirmation.html',{'my_appointment': my_appointment,},context)



def edit(request,pk):
	return HttpResponse('fuck you')


def register(request):
	context = RequestContext(request)

	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()

			registered = True
		else:
			print user_form.errors, profile_form.errors

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render_to_response('appt/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)



def user_login(request):
	context = RequestContext(request)

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username = username, password = password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/appt/')
			else:
				return HttpResponse("Your account is disabled.")
		else:
			print "Invalid login details {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")

	else:
		return render_to_response('appt/login.html', {}, context)




@login_required
def user_logout(request):
	logout(request)

	return HttpResponseRedirect('/appt/')













