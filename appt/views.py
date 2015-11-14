from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
	output = "Hello World!"

	return HttpResponse(output)


	