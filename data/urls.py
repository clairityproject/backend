from django.conf.urls import patterns, include, url
# this is the URL file for the API

from tastypie.api import Api
from data.api.resources import NodeResource, DataPointResource

v1_api = Api(api_name='v1')
v1_api.register(NodeResource())

urlpatterns = patterns('',
              (r'', include(v1_api.urls)),
              )
