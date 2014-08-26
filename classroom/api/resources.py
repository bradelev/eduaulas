from tastypie.resources import ModelResource, ALL
from classroom.models import ClassRoom, Grade
from tastypie.authorization import Authorization


class ClassRoomResource(ModelResource):
    class Meta:
    	authorization = Authorization()
        queryset = ClassRoom.objects.all()
        allowed_methods = ['get','post']

        filtering = {
        	'code': ALL,
        }

class GradeResource(ModelResource):
	class Meta:
		authorization =Authorization()
		queryset = Grade.objects.all()
		allowed_methods = ['get','post']

		filtering = {
			'name': ALL,
		}