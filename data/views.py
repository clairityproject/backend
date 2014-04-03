from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


# Create your views here.
@csrf_exempt
def secret_post(request):
    response_data = {}
    status = 400
    if request.method == "POST":
        print request.POST.items()
        #print dir(request.POST)
        #print request.POST.get('node_id')
        response_data['result'] = 'OK'
        status = 200
#class DataPoint(models.Model):
    ##node = models.ForeignKey(Node)
    #node_id = models.IntegerField(blank=False, null=False)
    #temperature = models.FloatField(null=True, blank=True)
    #rh = models.FloatField(null=True, blank=True) # relative humidity
    #dylos_bin_1 = models.FloatField(blank=True, null=True)
    #dylos_bin_2 = models.FloatField(blank=True, null=True)
    #dylos_bin_3 = models.FloatField(blank=True, null=True)
    #dylos_bin_4 = models.FloatField(blank=True, null=True)
    #alphasense_1 = models.FloatField(blank=True, null=True)
    #alphasense_2 = models.FloatField(blank=True, null=True)
    #alphasense_3 = models.FloatField(blank=True, null=True)
    #alphasense_4 = models.FloatField(blank=True, null=True)
    #alphasense_5 = models.FloatField(blank=True, null=True)
    #alphasense_6 = models.FloatField(blank=True, null=True)
    #alphasense_7 = models.FloatField(blank=True, null=True)
    #alphasense_8 = models.FloatField(blank=True, null=True)
    #reading_time = models.DateTimeField(blank=True, null=True)
    #added_on = models.DateTimeField(auto_now_add=True)
    #last_modified = models.DateTimeField(auto_now_add=True, auto_now=True)
    else:
        print "NOT POST"

    return HttpResponse(json.dumps(response_data), content_type="application/json", status=status)

