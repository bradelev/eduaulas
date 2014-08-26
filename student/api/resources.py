from tastypie.resources import ModelResource, ALL
from student.models import Student
from tastypie import fields
from tastypie.authorization import Authorization


class StudentResource(ModelResource):
	class Meta:
		authorization = Authorization()
		queryset = Student.objects.all()
		allowed_methods = ['get','post']
		filtering = {
			'serial': ALL,
		}