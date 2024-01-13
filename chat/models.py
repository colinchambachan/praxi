from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Chat(models.Model):
	content = models.CharField(max_length=1000)
	timestamp = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
	room = models.CharField(max_length=1000)
