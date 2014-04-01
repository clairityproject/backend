from tastypie.resources import ModelResource
from tastypie import fields
from data.models import IP, Node, DataPoint, Location
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS


class AqResource(ModelResource):
    class Meta:
        allowed_methods = ['post','get']

class IPResource(AqResource):
    class Meta:
        queryset = IP.objects.all()
	filtering={}
	for field in IP.__dict__['_meta'].fields:
	    filtering.update({field.name : ALL_WITH_RELATIONS})

class DataPointResource(AqResource):
    class Meta:
        queryset = DataPoint.objects.all()
	filtering={}
	for field in DataPoint.__dict__['_meta'].fields:
	    filtering.update({field.name : ALL_WITH_RELATIONS})

class LocationResource(AqResource):
    class Meta:
        queryset = Location.objects.all()
	filtering={}
	for field in Location.__dict__['_meta'].fields:
	    filtering.update({field.name : ALL_WITH_RELATIONS})

class NodeResource(AqResource):
    location = fields.ForeignKey(LocationResource, 'location',full=True)
    ip = fields.ForeignKey(IPResource, 'ip',full=True)
    class Meta:
        queryset = Node.objects.all()
	filtering={}
	for field in Node.__dict__['_meta'].fields:
	    filtering.update({field.name : ALL_WITH_RELATIONS})

