from django.urls import path
from . import views

urlpatterns = [
	path("", views.chatHome, name='chatHome'),
	path("<str:room_name>/", views.room, name='room'),
	path("fart/fart/", views.hello_world_page, name='fart'),
	path("User/aiChat/<str:lang>/<str:diff>", views.aiRoom, name='aiChat')
]