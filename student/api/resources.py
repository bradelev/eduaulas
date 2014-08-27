from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from student.models import Student
from classroom.models import ClassRoom
from classroom.api.resources import ClassRoomResource
from tastypie import fields
from tastypie.authorization import Authorization


class StudentResource(ModelResource):
	classroom = fields.ForeignKey(ClassRoomResource, 'class_room')
	class Meta:
		authorization = Authorization()
		queryset = Student.objects.all()
		resource_name = 'student'
		allowed_methods = ['get','post']
		filtering = {
			'serial': ALL,
			'classroom': ALL_WITH_RELATIONS,
		}