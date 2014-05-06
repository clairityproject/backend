from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from forms import DownloadForm


# Create your views here.

def index(request):
    return redirect('http://clairity.mit.edu/site/html/', permanent=True)

def export(request):
    form = DownloadForm()
    return render_to_response('export.html', {'form':form})

def my_custom_error_view(request):
    return render_to_response('500.html')
