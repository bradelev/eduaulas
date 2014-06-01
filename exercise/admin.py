from django.contrib import admin

# Register your models here.
from exercise.models import Result, Exercise, TeacherComments, Unit, Area, Topic
from location.models import School, Department, Country
from teacher.models import Teacher
from student.models import Student

# Register your models here.
admin.site.register(Result)
admin.site.register(Exercise)
admin.site.register(TeacherComments)
admin.site.register(Unit)
admin.site.register(Area)
admin.site.register(Topic)
admin.site.register(School)
admin.site.register(Department)
admin.site.register(Country)
admin.site.register(Teacher)
admin.site.register(Student)
