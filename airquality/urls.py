from django.conf.urls import patterns, include, url
from website.views import index

import data.urls as dataurls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'airquality.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #:::::::::::::::::::::::::::::
    #    API
    #:::::::::::::::::::::::::::::
    url(r'^node/postdata/','data.views.secret_post'),
    url(r'^api/', include(dataurls)),
    #:::::::::::::::::::::::::::::
    #    website
    #:::::::::::::::::::::::::::::
    url(r'^$', index , name='home'),

    #:::::::::::::::::::::::::::::
    #    admin
    #:::::::::::::::::::::::::::::
    url(r'^admin/', include(admin.site.urls)),
)
