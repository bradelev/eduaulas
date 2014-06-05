from django.db import models
# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext as _

# Create your models here.

class School(models.Model):
	number = models.IntegerField(default = 0, blank = True, verbose_name=u'Numero')
	name = models.CharField(max_length = 50, blank = True, verbose_name=u'Nombre')
	department = models.ForeignKey('Department', verbose_name=u'Departamento')

	class Meta:
		verbose_name = _('Escuela')
		verbose_name_plural = _('Escuelas')

	def __unicode__(self):
		return str(self.number) + " - " + self.name

class Department(models.Model):
	name = models.CharField(max_length=50, blank=True, verbose_name=u'Departamento')
	country = models.ForeignKey('Country', blank=True, verbose_name=u'País')

	class Meta:
		verbose_name = _('Departamento')
		verbose_name_plural = _('Departamentos')

	def __unicode__(self):
		return self.name

class Country(models.Model):
	name = models.CharField(max_length = 40, blank = True, verbose_name=u'Nombre')

	class Meta:
		verbose_name = _('Pais')
		verbose_name_plural = _('Paises')

	def __unicode__(self):
		return self.name

