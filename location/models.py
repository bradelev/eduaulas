from django.db import models

# Create your models here.

class School(models.Model):
	number = models.IntegerField(default = 0, blank = True)
	name = models.CharField(max_length = 50, blank = True)
	department = models.ForeignKey('Department')

class Department(models.Model):
	name = models.CharField(max_length = 50, blank = True)
	country = models.ForeignKey('Country')

class Country(models.Model):
	name = models.CharField(max_length = 40, blank = True)

