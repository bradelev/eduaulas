# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _


# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length = 50, verbose_name=u'Nombre')
	last_name = models.CharField(blank=True, max_length = 50, verbose_name=u'Apellido')
	date_of_birth = models.DateField(verbose_name=u'Fecha de nacimiento')
	tipo_choices = (
		('MALE', 'Masculino'), 
		('FEMALE', 'Femenino')
	)
	gender = models.CharField(choices=tipo_choices, max_length=10, verbose_name=u'Género')
	serial = models.CharField(blank=True, max_length=50, verbose_name=u'Numero de serie XO')