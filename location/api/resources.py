from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from location.models import Country, Department
from tastypie import fields
from tastypie.authorization import Authorization


class CountryResource(ModelResource):
    class Meta:
    	authorization = Authorization()
        queryset = Country.objects.all()
        allowed_methods = ['get','post']
        filtering = {
        	'name': ALL,
        }


class DepartmentResource(ModelResource):
	country = fields.ForeignKey(CountryResource, 'country')
	class Meta:
		authorization = Authorization()
		queryset = Department.objects.all()
		allowed_methods = ['get','post']
		filtering = {
			'country': ALL_WITH_RELATIONS,
		}
