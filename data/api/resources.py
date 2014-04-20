from tastypie.resources import ModelResource
from tastypie import fields
from data.models import DataPoint, Node
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
#from tastypie.authorization import Authorization
#from tastypie.authentication import Authentication


class AqResource(ModelResource):
    class Meta:
        allowed_methods = ['get']


class DataPointResource(AqResource):
    class Meta:
        queryset = DataPoint.objects.all()
    filtering={}
    #authorization = Authorization()
    #serializer = Serializer(formats=['json'])
    #authentication = Authentication()
    for field in DataPoint.__dict__['_meta'].fields:
        filtering.update({field.name : ALL_WITH_RELATIONS})


class NodeResource(AqResource):
    class Meta:
        queryset = Node.objects.all()
    filtering={}
    for field in Node.__dict__['_meta'].fields:
        filtering.update({field.name : ALL_WITH_RELATIONS})

