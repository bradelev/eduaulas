# -*- encoding: utf-8 -*-
from django.db import models
from person.models import Person
from django.utils.translation import ugettext as _

# Create your models here.
class Teacher(Person):
	email = models.EmailField(blank=True)
	nickname = models.CharField(max_length=50, verbose_name=u'Usuario')
	password = models.CharField(max_length=100, verbose_name=u'Contraseña')
	

	class Meta:
		verbose_name = _('Docente')
		verbose_name_plural = _('Docentes')

	def __unicode__(self):
		return self.name + " " + self.last_name



