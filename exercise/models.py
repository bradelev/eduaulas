from django.db import models
from student.models import Student
from classroom.models import Grade
from teacher.models import Teacher
from django.utils.translation import ugettext as _

# Create your models here.

class Result(models.Model):
	points = models.FloatField(null = True)
	answer = models.TextField(null=True)
	exercise = models.ForeignKey('Exercise')
	student = models.ForeignKey(Student)
	time_elapsed = models.IntegerField(blank=True)

	class Meta:
		verbose_name = _('Resultado')
		verbose_name_plural = _('Resultados')

	def __unicode__(self):
		return self.points


class Exercise(models.Model): 
	exercise_id = models.IntegerField(default=0)
	grade = models.ForeignKey(Grade)
	topic = models.ForeignKey('Topic', default="")
	unit = models.ForeignKey('Unit')  #A,B,C,D
	tipo_choices = (
		('TRUE_FALSE', 'Verdadero o Falso'), 
		('MULTIPLE_CHOICE', 'Multiple Opcion'), 
		('DRAG_AND_DROP', 'Arrastrar y Soltar'), 
		('CRUCIGRAMA', 'Crucigrama'),
		('FILL_BLANKS', 'Rellenar')
	)
	tipo = models.CharField(choices=tipo_choices, max_length=50)
	teacher_guide = models.TextField(max_length=1000, blank=True)
	img = models.ImageField(upload_to='media', blank=True)
	ejercicios_bien = models.ManyToManyField('self', blank=True)
	ejercicios_mal = models.ManyToManyField('self', blank=True)

	class Meta:
		verbose_name = _('Ejercicio')
		verbose_name_plural = _('Ejercicios')

	def __unicode__(self):
		return self.unit.letter + self.exercise_id

class TeacherComments(models.Model):
	teacher = models.ManyToManyField(Teacher)
	comments = models.TextField()
	exercise = models.ForeignKey('Exercise')

	class Meta:
		verbose_name = _('Comentario del docente')
		verbose_name_plural = _('Comentarios del docente')

	def __unicode__(self):
		return self.teacher.name + " " + self.teacher.lastname
    

#UNIDAD A, B, C, etc...
class Unit(models.Model):
	letter = models.CharField(max_length=1) #A,B,C, etc
	name = models.CharField(blank=True, max_length=150) 
	description = models.TextField(blank=True, max_length=200) # EXPLICACION DE LA UNIDAD
	topic = models.ForeignKey('Topic')
	available = models.BooleanField(default=True)


	class Meta:
		verbose_name = _('Unidad')
		verbose_name_plural = _('Unidades')

	def __unicode__(self):
		pass

#CIENCIAS NATURALES, ARTISTICA, CIENCIAS SOCIALES, MATEMATICA, LENGUA
class Area(models.Model):
	name = models.CharField(max_length=50)

	class Meta:
		verbose_name = _('Area')
		verbose_name_plural = _('Areas')

	def __unicode__(self):
		pass
    
#FISICA, QUIMICA, GEOLOGIA    
class Topic(models.Model):
	name = models.CharField(max_length=50)

	class Meta:
		verbose_name = _('Materia')
		verbose_name_plural = _('Materias')

	def __unicode__(self):
		pass
    