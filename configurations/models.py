from django.db import models
from teacher.models import Teacher
from django.utils.translation import ugettext as _

# Create your models here.

class Configuration(models.Model):

	teacher = models.ForeignKey(Teacher, null=True, blank=True)
	incorrect_points = models.FloatField(default = 0.3, blank = True, verbose_name=u'Puntaje ejercicio sea incorrecto')
	correct_points = models.FloatField(default = 0.85, blank = True, verbose_name=u'Puntaje ejercicio sea correcto')
	minimum_quantity_exercise = models.IntegerField(default = 3, blank = True, verbose_name=u'Cantidad de ejercicios minimos')