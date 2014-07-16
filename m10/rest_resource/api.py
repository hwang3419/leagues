from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from models import Test

class TestResource(ModelResource):
    class Meta:
        queryset = Test.objects.all()
        resource_name = 'test' 
        authorization= Authorization()