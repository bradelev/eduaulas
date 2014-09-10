# -*- encoding: utf-8 -*-
from django.db import models

from django.utils.translation import ugettext as _


# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length = 50, verbose_name=u'Nombre', null=True)
	last_name = models.CharField(blank=True, max_length = 50, verbose_name=u'Apellido', null=True)
	date_of_birth = models.DateField(blank=True, verbose_name=u'Fecha de nacimiento', null=True)
	type_choices = (
		('1', 'Masculino'), 
		('2', 'Femenino'),
		('3', 'No desea responder')
	)
	gender = models.CharField(choices=type_choices, max_length=10, verbose_name=u'Género', null=True)
	serial = models.CharField(blank=True, max_length=50, verbose_name=u'Numero de serie XO', unique=True, null=True)
	created = models.DateTimeField(auto_now=True, blank=True, verbose_name=u'Fecha de creación')
	updated = models.DateTimeField(auto_now=True, blank=True, verbose_name=u'Fecha de update')

	def __unicode__(self):
		return self.name + " " + self.last_name