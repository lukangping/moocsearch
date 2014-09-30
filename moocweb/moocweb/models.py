from django.db import models

class Course(models.Model):
	
	cid = models.CharField(max_length=100)
	title = models.CharField(max_length=500)
	link = models.CharField(max_length=300)
	

