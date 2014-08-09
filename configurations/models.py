from django.db import models
from teacher.models import Teacher
from django.utils.translation import ugettext as _

# Create your models here.

class Configuration(models.Model):
	teacher = models.ForeignKey(Teacher, null=True, blank=True)

