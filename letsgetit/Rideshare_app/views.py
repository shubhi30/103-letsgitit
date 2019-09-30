from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the RideShare index.")

def search(request):
	return render(request, 'Rideshare_app/search.html')

def profile(request):
	return  HttpResponse("Profile Page")
