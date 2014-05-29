from django.db import models
from alumno.models import Alumno

# Create your models here.

class Resultado(models.Model):
	puntos_obtenidos = models.FloatField(null = True)
	respuesta = models.TextField(null=True)
	ejercicio = models.ForeignKey('Ejercicio')
	alumno = models.ForeignKey(Alumno)


class Ejercicio(models.Model):
	nombre = models.CharField(max_length = 100)
	grado = models.CharField(max_length = 10)
	unidad = models.CharField(max_length = 1)
	tipo_choices = (
		('TRUE_FALSE', 'Verdadero o Falso'), 
		('MULTIPLE_CHOICE', 'Multiple Opcion'), 
		('DRAG_AND_DROP', 'Arrastrar y Soltar'), 
		('CRUCIGRAMA', 'Crucigrama'),
		('FILL_BLANKS', 'Rellenar')
	)
	tipo = models.CharField(choices = tipo_choices, max_length = 50)
