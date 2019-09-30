from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the RideShare index.")

def search(request):
	return HttpResponse("Display search results!")

def login(request):
	return HttpResponse("Display login!")
