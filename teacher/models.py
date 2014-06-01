from django.db import models

# Create your models here.
class Teacher(models.Model):
	name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	nickname = models.CharField(max_length=50)
	password = models.CharField(max_length=100)
	date_of_birth = models.DateField()
	gender = models.BooleanField()

	serial = models.CharField(blank=True, max_length=50)


