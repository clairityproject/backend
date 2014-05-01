from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from forms import DownloadForm


# Create your views here.

def index(request):
    return render_to_response('in_progress.html')

def export(request):
    form = DownloadForm()
    return render_to_response('export.html', {'form':form})

def my_custom_error_view(request):
    return render_to_response('500.html')
