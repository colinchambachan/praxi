from django.shortcuts import render, redirect

# Create your views here.
def landing(request):
	return render(request,"landing.html",{})

def chatHome(request):
	return render(request,"chatHome.html",{})

def about(request):
	return render(request,"about.html",{})

def login(request):
	pass
