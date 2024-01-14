from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Chat(models.Model):
	content = models.CharField(max_length=1000)
	timestamp = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
	room = models.CharField(max_length=1000)

class aiChat(models.Model):
	content = ArrayField(models.CharField(max_length=1000), null=True, blank=True)
	language = models.CharField(max_length=50)
	difficulty = models.CharField(max_length=20)
	user = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
	belongs_to = models.CharField(max_length=50, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now=True)