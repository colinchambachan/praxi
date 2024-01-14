from django.shortcuts import render
from .models import Chat, aiChat
from openai import OpenAI
from dotenv import load_dotenv
import os

# Create your views here.
def chatHome(request):
	return render(request, "chatHome.html")

# def aiChat(request):
# 	return render(request, "ai_room.html")

def room(request, room_name):
	chat_log = Chat.objects.filter(room=room_name).order_by('timestamp')
	return render(request, "room.html", {"room_name": room_name, "chat_log": chat_log, "username": request.user.username})

def aiRoom(request, lang, diff):
	if request.method == 'POST':
		content = request.POST.get('message')

		#Finds chat object with parameters of the user, difficulty, and language
		#Chats are unique, as if visiting the page will either display the existing object, or create new object (see else statement)	
		chatForm = aiChat.objects.get(belongs_to=request.user.username, difficulty=diff, language=lang)
		convo = chatForm.content

		#Appends user tags  to text to use as context for gpt generation
		convo.append("Me: "+content)

		try:
			load_dotenv()
			key = os.getenv('OPENAI_API_KEY')
			client = OpenAI(api_key=key)
			user_content = "\n".join(convo)
			sys_content = "You are a friendly chatter and language tutor named Prax, participating in a "+diff+ " conversation in "+lang+", and I will give you the chat history of a conversation we had. we are both speaking in English. my words are prefixed with 'Me:'.  Please reply with your response, do NOT append your message with anything at the start of your response. Limit your responses to a max of 30 words, but try to keep it pretty consise. Try to sprinkle in some uncommon words to facilitate language learning!"
			
			response = client.chat.completions.create(
				model="gpt-3.5-turbo",
				messages=[
					{"role": "system", "content": sys_content},
					{"role": "user", "content": user_content}
				]
			)
			#Appends gpt message + tag and saves to object
			convo.append("AI: "+response.choices[0].message.content)
			chatForm.content = convo
			chatForm.save()	

			return render(request, "ai_room.html", {"content": convo, "language": lang})
		except:
			#IN FUTURE REDIRECT BACK TO LANDING
			return render(request, "ai_room.html", {"content": convo, "language": lang})
	else:
		#will return exception if object does not exist, which requires the object to be created
		try:
			convo = aiChat.objects.get(belongs_to=request.user.username, difficulty=diff, language=lang).content
		except:
			convoInstance = aiChat(belongs_to=request.user.username, difficulty=diff, language=lang, content=[])
			convoInstance.save()
			return render(request, "ai_room.html", {"content": convoInstance.content, "language": lang})
		return render(request, "ai_room.html", {"content": convo, "language": lang})