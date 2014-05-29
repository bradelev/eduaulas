from django.db import models

# Create your models here.

class Escuela(models.Model):
	numero = models.IntegerField(default = 0, blank = True)
	nombre = models.CharField(max_length = 50, blank = True)
	departamento = models.ForeignKey('Departamento')

class Departamento(models.Model):
	nombre = models.CharField(max_length = 50, blank = True)
	pais = models.ForeignKey('Pais')

class Pais(models.Model):
	nombre = models.CharField(max_length = 40, blank = True)
