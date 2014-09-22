from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from models import Test, SP1, E0, I1, D1
import json
from django.core.serializers.json import DjangoJSONEncoder
from tastypie.serializers import Serializer
from tastypie.throttle import BaseThrottle
from tastypie.cache import SimpleCache
fillter = {
            'HomeTeam' : ALL_WITH_RELATIONS, 
            'AwayTeam' : ALL_WITH_RELATIONS,
            'FTR' :  ALL_WITH_RELATIONS,
            'AR' :  ALL_WITH_RELATIONS,
            'HR' :  ALL_WITH_RELATIONS,
            'HST' :  ALL_WITH_RELATIONS,
            'AST' :  ALL_WITH_RELATIONS,
            'HS' :  ALL_WITH_RELATIONS,
            'AS' :  ALL_WITH_RELATIONS,
            'HY' :  ALL_WITH_RELATIONS,
            'AY' :  ALL_WITH_RELATIONS,
            'HC' :  ALL_WITH_RELATIONS,
            'AC' :  ALL_WITH_RELATIONS,
            'B365H' :  ALL_WITH_RELATIONS,
            'B365D' :  ALL_WITH_RELATIONS,
            'B365A' :  ALL_WITH_RELATIONS,
            'Date': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }


class PrettyJSONSerializer(Serializer):
    json_indent = 2

    def to_json(self, data, options=None):
        options = options or {}
        data = self.to_simple(data, options)
        return json.dumps(data, cls=DjangoJSONEncoder,
                sort_keys=True, ensure_ascii=False, indent=self.json_indent)

class TestResource(ModelResource):
    class Meta:
        queryset = Test.objects.all()
        resource_name = 'test' 
        authorization= Authorization()

class baseMeta:
    authorization= Authorization()
    excludes = []
    allowed_methods = ['get']
    ordering = ['Date','FTR','AR','HR','HST','AST','HS','AS','HY','AY','HC','AC','B365H','B365D','B365A']
    filtering = fillter
    serializer = PrettyJSONSerializer()
    throttle = BaseThrottle(throttle_at=500)
    cache = SimpleCache(timeout=10000)

class SP1Resource(ModelResource):
    class Meta(baseMeta):
        queryset = SP1.objects.all()
        resource_name = 'sp1'    

class E0Resource(ModelResource):
    class Meta(baseMeta):
        queryset = E0.objects.all()
        resource_name = 'e0' 

class D1Resource(ModelResource):
    class Meta(baseMeta):
        queryset = D1.objects.all()
        resource_name = 'd1' 

class I1Resource(ModelResource):
    class Meta(baseMeta):
        queryset = I1.objects.all()
        resource_name = 'i1' 