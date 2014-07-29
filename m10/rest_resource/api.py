from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from models import Test, SP1, E0, I1

fillter = {
            'HomeTeam': ALL   
        }
class TestResource(ModelResource):
    class Meta:
        queryset = Test.objects.all()
        resource_name = 'test' 
        authorization= Authorization()

class SP1Resource(ModelResource):
    class Meta:
        queryset = SP1.objects.all()
        resource_name = 'sp1' 
        authorization= Authorization()
        excludes = []
        allowed_methods = ['get']
        filtering = fillter

class E0Resource(ModelResource):
    class Meta:
        queryset = E0.objects.all()
        resource_name = 'e0' 
        authorization= Authorization()
        excludes = []
        allowed_methods = ['get']
        filtering = fillter

class D1Resource(ModelResource):
    class Meta:
        queryset = E0.objects.all()
        resource_name = 'd1' 
        authorization= Authorization()
        excludes = []
        allowed_methods = ['get']
        filtering = fillter

class I1Resource(ModelResource):
    class Meta:
        queryset = E0.objects.all()
        resource_name = 'i1' 
        authorization= Authorization()
        excludes = []
        allowed_methods = ['get']
        filtering = fillter