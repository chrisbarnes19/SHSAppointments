from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from django.contrib.auth import authenticate, login, logout

from .models import Appointment
from .forms import UserForm, UserProfileForm

# Create your views here.


def index(request):
	output = "Hello World!"

	return HttpResponse(output)


def monthly_view(request, month):
	
	return HttpResponse('hello')


def date_view(request,date):
	return HttpResponse('hello')


def new_appointment(request,date):
	return HttpResponse('dicks')

def confirmation(request,pk):
	return HttpResponse('fuck you')

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













