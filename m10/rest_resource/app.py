from tastypie.resources import ModelResource
from models import Entry

class LeagueResource(ModelResource):
    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'