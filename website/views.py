from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.views.generic.base import TemplateView
from forms import DownloadForm

#def index(request):
    #return redirect('http://clairity.mit.edu/site/html/', permanent=True)

#def export(request):
    #form = DownloadForm()
    #return render_to_response('export.html', {'form':form})

class ClairityView(TemplateView):
    page_name = None

    def get_context_data(self, **kwargs):
        context = super(ClairityView, self).get_context_data(**kwargs)
        page_name = self.page_name or self.template_name.split('.')[0].capitalize() + ' Page'
        context['name'] = page_name
        context['title'] = page_name
        return context

class ExportPageView(ClairityView):
    template_name = "export.html"

export = ExportPageView.as_view()

class HomePageView(ClairityView):
    template_name = "home.html"

home = HomePageView.as_view()

class HowItWorksPageView(ClairityView):
    page_name = 'How it works'
    template_name = "howitworks.html"

how_it_works = HowItWorksPageView.as_view()

class IndexPageView(ClairityView):
    template_name = "index.html"

index = IndexPageView.as_view()

class MuseumPageView(ClairityView):
    template_name = "museum.html"

museum = MuseumPageView.as_view()

class ProjectPageView(ClairityView):
    template_name = "project.html"

project = ProjectPageView.as_view()

class TeamPageView(ClairityView):
    template_name = "team.html"

team = TeamPageView.as_view()

def my_custom_error_view(request):
    return render_to_response('500.html')

