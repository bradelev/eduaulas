# -*- encoding: utf-8 -*-
from django.db import models
from student.models import Student
from person.models import Person
from classroom.models import Grade
from teacher.models import Teacher
from django.utils.translation import ugettext as _

# Create your models here.



class Lecture(models.Model):
	cuasimodo_lecture_id = models.IntegerField(default=0, verbose_name = u'ID Cuasimodo', blank = True)
	name = models.CharField(max_length=100, blank=True, null=True)
	grade = models.ForeignKey(Grade, verbose_name=u'Grado', blank = True)
	unit = models.ForeignKey('Unit', verbose_name=u'Unidad')  #A,B,C,D - es el link a materia
	teacher_guide = models.TextField(max_length=2000, blank=True, verbose_name=u'Guía docente')
	img = models.ImageField(upload_to='media', blank=True, verbose_name=u'Imágen')
	LectureType = (
		('EXPERIMENT', 'Experimento'), 
		('LECTURE', 'Lecturas'), 
		('BOOK_ACTIVITY', 'Actividades escritas'),
		('HOMEWORK', 'Tareas')
	)
	lecture_type = models.CharField(choices=LectureType, max_length=50, verbose_name=u'Tipo de página')
	class Meta:
		verbose_name = _('Lectura')
		verbose_name_plural = _('Lecturas')

	def __unicode__(self):
		return self.exercise_id

class Exercise(models.Model): 
	cuasimodo_exercise_id = models.IntegerField(default=0, verbose_name=u'ID Cuasimodo', blank = True)
	name = models.CharField(max_length=100, blank=True, null=True)
	grade = models.ForeignKey(Grade, verbose_name=u'Grado', blank = True)
	unit = models.ForeignKey('Unit', verbose_name=u'Unidad')  #A,B,C,D - es el link a materia
	ExerciseType = (
		('TRUE_FALSE', 'Verdadero o Falso'), 
		('MULTIPLE_CHOICE', 'Multiple Opcion'), 
		('DRAG_AND_DROP', 'Arrastrar y Soltar'), 
		('CRUCIGRAMA', 'Crucigrama'),
		('FILL_BLANKS', 'Rellenar')
	)
	exercise_type = models.CharField(choices=ExerciseType, max_length=50, verbose_name=u'Tipo de ejercicio', null=True)
	teacher_guide = models.TextField(max_length=2000, blank=True, verbose_name=u'Guía docente', null=True)
	img = models.ImageField(upload_to='media', blank=True, verbose_name=u'Imágen', null=True)
	good_related_exercises = models.ManyToManyField('self', blank=True, verbose_name=u'Ejercicios relacionados bien', null=True)
	bad_related_exercises = models.ManyToManyField('self', blank=True, verbose_name=u'Ejercicios relacionados mal', null=True)
	metacognitive_percentage = models.FloatField(default=0, verbose_name=u'Porcentaje meta congnitivo', blank = True, null=True)
	cognitive_percentage=models.FloatField(default=0, verbose_name=u'Porcentaje congnitivo', blank = True, null=True)
	socio_affective_percentage=models.FloatField(default=0, verbose_name=u'Porcentaje socio afectivo', blank = True, null=True)
	

	class Meta:
		verbose_name = _('Ejercicio')
		verbose_name_plural = _('Ejercicios')

	#def __unicode__(self):
	#	return self.exercise_id

class Result(models.Model):
	points = models.FloatField(null = True, verbose_name=u'Puntos')
	answer = models.TextField(null=True, verbose_name=u'Respuesta')
	exercise = models.ForeignKey(Exercise, verbose_name=u'Ejercicio')
	person = models.ForeignKey(Person, verbose_name=u'Persona')
	time_elapsed = models.FloatField(blank=True, verbose_name=u'Tiempo de realización')
	created = models.DateTimeField(auto_now=True, blank=True, verbose_name=u'Fecha de creación')
	updated = models.DateTimeField(auto_now=True, blank=True, verbose_name=u'Fecha de update')

	class Meta:
		verbose_name = _('Resultado')
		verbose_name_plural = _('Resultados')

	def __unicode__(self):
		return self.points


class TeacherComments(models.Model):
	teacher = models.ForeignKey(Teacher, verbose_name=u'Docente', blank=True, null=True)
	comments = models.TextField(verbose_name=u'Comentario')
	exercise = models.ForeignKey('Exercise', verbose_name=u'Ejercicio')
	lecture = models.ForeignKey('Lecture', verbose_name=u'Lectura')
	created = models.DateTimeField(auto_now=True, blank=True, verbose_name=u'Fecha de creación')
	updated = models.DateTimeField(auto_now=True, blank=True, verbose_name=u'Fecha de update')

	class Meta:
		verbose_name = _('Comentario del docente')
		verbose_name_plural = _('Comentarios del docente')

	def __unicode__(self):
		return self.teacher.name + " " + self.teacher.lastname
    

#UNIDAD A, B, C, etc...
class Unit(models.Model):
	letter = models.CharField(max_length=1, verbose_name=u'Letra de unidad') #A,B,C, etc
	name = models.CharField(blank=True, max_length=150, verbose_name=u'Nombre') 
	description = models.TextField(blank=True, max_length=200, verbose_name=u'Descripción') # EXPLICACION DE LA UNIDAD
	subject = models.ForeignKey('Subject', verbose_name=u'Materia')
	available = models.BooleanField(default=True, verbose_name=u'Habilitada')
	grade = models.ForeignKey(Grade, verbose_name=u'Grado', blank = True)

	class Meta:
		verbose_name = _('Unidad')
		verbose_name_plural = _('Unidades')

	def __unicode__(self):
		return self.letter + ". " + self.name

#CIENCIAS NATURALES, ARTISTICA, CIENCIAS SOCIALES, MATEMATICA, LENGUA
class Area(models.Model):
	name = models.CharField(max_length=50, verbose_name=u'Area', unique=True)

	class Meta:
		verbose_name = _('Area')
		verbose_name_plural = _('Areas')

	def __unicode__(self):
		return self.name
    
#FISICA, QUIMICA, GEOLOGIA    
class Subject(models.Model):
	name = models.CharField(max_length=50, verbose_name=u'Materia', unique=True)
	area= models.ForeignKey('Area', verbose_name=u'Area')
	class Meta:
		verbose_name = _('Materia')
		verbose_name_plural = _('Materias')

	def __unicode__(self):
		return self.name    
