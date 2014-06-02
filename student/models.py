from django.db import models
from person.models import Person

# Create your models here.
class Student(models.Model):
	person = models.ForeignKey(Person)