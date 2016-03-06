from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

# Create your models here.
class Messages(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	sender = models.CharField(max_length=100)
	text = models.TextField(max_length=1000)
	
	def __str__(self):
		return self.sender