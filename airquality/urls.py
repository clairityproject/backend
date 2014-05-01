from django.conf.urls import patterns, include, url, handler404, handler500
from website.views import index

import data.urls as dataurls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'airquality.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #:::::::::::::::::::::::::::::
    #    API (coding team)
    #:::::::::::::::::::::::::::::
    url(r'^node/postdata/$','data.views.secret_post'),
    url(r'^node/postdata/dylos','data.views.secret_post_dylos'),
    url(r'^node/postdata/met','data.views.secret_post_met'),
    url(r'^node/postdata/alphasense','data.views.secret_post_alphasense'),
    url(r'^api/', include(dataurls)),

    #:::::::::::::::::::::::::::::
    #    website
    #:::::::::::::::::::::::::::::
    url(r'^$', index , name='home'),
    url(r'^export/', 'website.views.export', name='export'),

    #:::::::::::::::::::::::::::::
    #    admin
    #:::::::::::::::::::::::::::::
    url(r'^admin/', include(admin.site.urls)),

    #:::::::::::::::::::::::::::::
    #    API (front-end team)
    #:::::::::::::::::::::::::::::
    url(r'^latest/all/$', 'data.views.get_latest_now_fix'),
    url(r'^latest/$', 'data.views.get_latest'),
    url(r'^latest/hour/$', 'data.views.get_latest', {'hour':True} ),
    url(r'^latest/day/$', 'data.views.get_latest', {'day':True} ),
    url(r'^latest/week/$', 'data.views.get_latest', {'week':True} ),
    url(r'^graph/all','data.views.graph_data'),
    url(r'^download/csv/', 'data.views.download_csv'),
)

handler500 = 'website.views.my_custom_error_view'
handler404 = 'website.views.my_custom_error_view'
