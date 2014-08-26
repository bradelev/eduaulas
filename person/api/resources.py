from tastypie.resources import ModelResource, ALL
from person.models import Person
from tastypie import fields
from tastypie.authorization import Authorization


class PersonResource(ModelResource):
	class Meta:
		authorization = Authorization()
		queryset = Person.objects.all()
		allowed_methods = ['get','post']
		filtering = {
			'serial': ALL,
		}