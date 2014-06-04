# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from teacher.models import Teacher
from location.models import School



# Create your models here.
class ClassRoom(models.Model):
	code = models.CharField(max_length = 5, verbose_name=u'Código de aula', primary_key=True) #CODIGO DE ACCESO AL AULA	
	class_letter = models.CharField(max_length=3, verbose_name=u'Letra de clase') #A, B, C...
	shift_choices = (
		('OTHER', 'Otro'), 
		('MORNING', 'Matutino'), 
		('EVENING', 'Vespertino'), 
		('FULL_TIME', 'Tiempo Completo')
	)
	shift = models.CharField(max_length = 20, choices = shift_choices, verbose_name=u'Turno')
	grade = models.ForeignKey('Grade', verbose_name=u'Grado')
	teachers = models.ManyToManyField(Teacher, verbose_name=u'Docente')
	school = models.ForeignKey(School, verbose_name=u'Escuela')

	class Meta:
		verbose_name = _('Aula')
		verbose_name_plural = _('Aulas')

	def __unicode__(self):
		return str(self.grade.name) + unicode('°', encoding='utf-8') + self.class_letter + ' Escuela Num ' + str(self.school.number)

	

class Grade(models.Model):
	name = models.IntegerField(default = 0, blank = True, verbose_name=u'Año')

	class Meta:
		verbose_name = _('Grado')
		verbose_name_plural = _('Grados')

	def __unicode__(self):
		return unicode(self.name) 





