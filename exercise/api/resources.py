from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from exercise.models import Exercise, Result, TeacherComments, Unit, Subject
from student.models import Student
from person.api.resources import PersonResource
from classroom.models import Grade
from classroom.api.resources import GradeResource
from student.api.resources import StudentResource
from tastypie import fields
from tastypie.authorization import Authorization




class SubjectResource(ModelResource):
	class Meta:
		authorization = Authorization()
		queryset = Subject.objects.all()
		allowed_methods = ['get','post']
		filtering = {
			'name':ALL,
		}

		

class UnitResource(ModelResource):
	subject = fields.ForeignKey(SubjectResource, 'subject')
	grade = fields.ForeignKey(GradeResource, 'grade')
	class Meta:
		authorization = Authorization()
		queryset = Unit.objects.all()
		resource_name = 'unit'
		allowed_methods = ['get','post']
		filtering = {
			'letter': ALL,
			'subject': ALL_WITH_RELATIONS,
			'grade': ALL_WITH_RELATIONS,
		}


class ExerciseResource(ModelResource):
	unit = fields.ForeignKey(UnitResource, 'unit')

	class Meta:
		authorization = Authorization()
		queryset = Exercise.objects.all()
		resource_name = 'exercise'
		allowed_methods = ['get','post']
		filtering = {
			'cuasimodo_exercise_id': ALL,
			'name':ALL,
			'unit': ALL_WITH_RELATIONS,
        }

class ResultResource(ModelResource):
	person = fields.ForeignKey(PersonResource, 'person')
	exercise = fields.ForeignKey(ExerciseResource, 'exercise')
	class Meta:
		authorization = Authorization()
		queryset = Result.objects.all()
		allowed_methods = ['get','post']
		filtering = {
			'person': ALL_WITH_RELATIONS,
			'exercise': ALL_WITH_RELATIONS,
		}



class TeacherCommentsResource(ModelResource):
    class Meta:
    	authorization = Authorization()
        queryset = TeacherComments.objects.all()
        allowed_methods = ['post']        