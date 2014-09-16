from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^home', views.home, name='home'),
        url(r'^export', views.export, name='export'),
        url(r'^howitworks', views.how_it_works, name='how_it_works'),
        url(r'^museum', views.museum, name='museum'),
        url(r'^project', views.project, name='project'),
        url(r'^team', views.team, name='team'),
)
