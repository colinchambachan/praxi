from django.shortcuts import render
from .models import Chat
# from react_templates.render import render_react

def hello_world_page(request):
	pass
    # return render_react(request, "chat/HelloWorld.js") # Notice you must not mention the web folder!
# Create your views here.
def chatHome(request):
	return render(request, "chatHome.html")

def room(request, room_name):
	chat_log = Chat.objects.filter(room=room_name).order_by('timestamp')
	return render(request, "room.html", {"room_name": room_name, "chat_log": chat_log})
