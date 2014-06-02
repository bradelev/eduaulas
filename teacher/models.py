from django.db import models
from person.models import Person

# Create your models here.
class Teacher(models.Model):
	person = models.ForeignKey(Person)
	nickname = models.CharField(max_length=50)
	password = models.CharField(max_length=100)
	


