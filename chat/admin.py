from django.contrib import admin
from .models import Chat

class ChatAdmin(admin.ModelAdmin):
	list_display = ['content', 'room']
# Register your models here.
admin.site.register(Chat, ChatAdmin)