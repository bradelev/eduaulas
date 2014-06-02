from django.db import models


# Create your models here.
class ClassRoom(models.Model):
	code = models.CharField(max_length = 5)
	class_letter = models.CharField(max_length = 3) #A, B, C...
	shift_choices = (
		('OTHER', 'Otro'), 
		('MORNING', 'Matutino'), 
		('EVENING', 'Vespertino'), 
		('FULL_TIME', 'Tiempo Completo')
	)
	shift = models.CharField(max_length = 20, choices = shift_choices)

	#escuela = 

class Grade(models.Model):
	name = models.IntegerField(default = 0, blank = True)





