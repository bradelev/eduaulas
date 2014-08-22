from tastypie.resources import ModelResource
from location.models import Country
from tastypie.authorization import Authorization


class CountryResource(ModelResource):
    class Meta:
    	authorization = Authorization()
        queryset = Country.objects.all()
        allowed_methods = ['post']
       