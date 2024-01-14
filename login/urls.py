from django.urls import path, include
from . import views

urlpatterns = [
	path("", views.landing, name='landing'),
	path("login/", views.login, name='login'),
	path("about/", views.about, name='about')
	
]