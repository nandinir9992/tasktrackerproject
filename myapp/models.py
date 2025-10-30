from django.db import models

# Create your models here.
class task(models.Model):
	title=models.CharField(max_length=90)
	description=models.CharField(max_length=200)
	duedate=models.DateField()
	status=models.CharField(max_length=50)