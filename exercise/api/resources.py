from tastypie.resources import ModelResource
from exercise.models import Result, TeacherComments
from tastypie.authorization import Authorization


class ResultResource(ModelResource):
    class Meta:
    	authorization = Authorization()
        queryset = Result.objects.all()
        allowed_methods = ['post']

class TeacherCommentsResource(ModelResource):
    class Meta:
    	authorization = Authorization()
        queryset = TeacherComments.objects.all()
        allowed_methods = ['post']        