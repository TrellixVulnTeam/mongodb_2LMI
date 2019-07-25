from django.db import models
from djongo import models
# Create your models here.

class people_output(models.Model):
	_id = models.TextField(primary_key = True)
	signup = models.TextField()
	points = models.IntegerField(max_length=11)
	name = models.CharField(max_length=64)


class search(models.Model):
	_id = models.TextField(primary_key=True)
	signup = models.DateTimeField()
	points = models.IntegerField(max_length=11)
	name = models.CharField(max_length=64)
