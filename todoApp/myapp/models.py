from django.db import models

# Create your models here.
class ToDo(models.Model):
	task = models.CharField(max_length = 100)
	time = models.DateTimeField()