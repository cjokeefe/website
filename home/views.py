from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'home/home.html')


def about(request):
	return render(request, 'home/about.html')


def projects(request):
	return render(request, 'home/projects.html')

def misc(request):
	return render(request, 'home/misc.html')

def gradient(request):
	return render(request, 'home/gradientGen.html')