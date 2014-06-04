# -*- encoding: utf-8 -*-
from django.db import models
from classroom.models import ClassRoom
from person.models import Person
from django.utils.translation import ugettext as _

# Create your models here.
class Student(Person):
	class_room = models.ForeignKey(ClassRoom,verbose_name=u'Aula')
	
	


	class Meta:
		verbose_name = _('Estudiante')
		verbose_name_plural = _('Estudiantes')

	def __unicode__(self):
		return self.name + " " + self.last_name