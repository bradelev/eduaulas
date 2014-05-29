from django.db import models


# Create your models here.
class Aulas(models.Model):
	codigo = models.CharField(max_length = 5)
	clase = models.CharField(max_length = 3) #A, B, C...
	turno_choices = (
		('OTRO', 'Otro'), 
		('MATUTINO', 'Matutino'), 
		('VESPERTINO', 'Vespertino'), 
		('TIEMPO_COMPLETO', 'Tiempo Completo')
	)
	turno = models.CharField(max_length = 20, choices = turno_choices)

	#escuela = 

class Grado(models.Model):
	nombre = models.IntegerField(default = 0, blank = True)





