from django.db import models
from person.models import Person
from django.utils.translation import ugettext as _

# Create your models here.
class Student(Person):
	
	class Meta:
		verbose_name = _('Estudiante')
		verbose_name_plural = _('Estudiantes')

	def __unicode__(self):
		return super.name + " " + super.last_name