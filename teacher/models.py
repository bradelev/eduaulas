# -*- encoding: utf-8 -*-
from django.db import models
from person.models import Person
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

# Create your models here.
class Teacher(Person):
	user = models.OneToOneField(User) 
	

	class Meta:
		verbose_name = _('Docente')
		verbose_name_plural = _('Docentes')

	def __unicode__(self):
		return self.name + " " + self.last_name



