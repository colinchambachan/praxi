from django.shortcuts import render
from react_templates.render import render_react

def hello_world_page(request):
	pass
    # return render_react(request, "chat/HelloWorld.js") # Notice you must not mention the web folder!
# Create your views here.
def chatHome(request):
	return render(request, "chatHome.html")

def room(request, room_name):
	return render(request, "room.html", {"room_name": room_name})
