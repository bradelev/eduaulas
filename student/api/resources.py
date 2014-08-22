from tastypie.resources import ModelResource
from student.models import Student
from tastypie.authorization import Authorization


class StudentResource(ModelResource):
    class Meta:
    	authorization = Authorization()
        queryset = Student.objects.all()
        allowed_methods = ['post']