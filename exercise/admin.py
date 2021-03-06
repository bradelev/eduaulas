from django.contrib import admin

# Register your models here.
from classroom.models import ClassRoom, Grade
from exercise.models import Result, Exercise, TeacherComments, Unit, Area, Subject, Lecture
from location.models import School, Department, Country
from teacher.models import Teacher
from student.models import Student
from person.models import Person
from configurations.models import Configuration


# Register your models here.
admin.site.register(Result)
admin.site.register(Exercise)
admin.site.register(Lecture)
admin.site.register(TeacherComments)
admin.site.register(Unit)
admin.site.register(Area)
admin.site.register(Subject)
admin.site.register(School)
admin.site.register(Department)
admin.site.register(Country)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(ClassRoom)
admin.site.register(Configuration)
admin.site.register(Person)
