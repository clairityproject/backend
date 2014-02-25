from tastypie.resources import ModelResource
from data.models import IP, Node, DataPoint


class AqResource(ModelResource):
    class Meta:
        allowed_methods = ['post','get']

class NodeResource(AqResource):
    class Meta:
        queryset = Node.objects.all()

class IPResource(AqResource):
    class Meta:
        queryset = IP.objects.all()
class DataPointResource(AqResource):
    class Meta:
        queryset = DataPoint.objects.all()
