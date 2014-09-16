from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from data.models import DataPoint, Met, Alphasense, Dylos, Node, Latest
import json
import datetime
import time
from admin import export_as_csv
from django.contrib.admin import ModelAdmin

#------------------------------------------------------------
#  Post Entries for the coding team
#------------------------------------------------------------

@csrf_exempt
def secret_post(request):
    """Function left for legacy reasons. TODO: remove after db migration"""
    response_data = {}
    status = 400
    if request.method == "POST":
        print request.POST.items()
        response_data['result'] = 'OK'
        status = 200

        try:
            point = DataPoint(
                    node_id = request.POST.get('node_id'),
                    temperature = request.POST.get('temperature'),
                    rh = request.POST.get('rh'),
                    dylos_bin_1 = request.POST.get('dylos_bin_1'),
                    dylos_bin_2 = request.POST.get('dylos_bin_2'),
                    dylos_bin_3 = request.POST.get('dylos_bin_3'),
                    dylos_bin_4 = request.POST.get('dylos_bin_4'),
                    alphasense_1 = request.POST.get('alphasense_1'),
                    alphasense_2 = request.POST.get('alphasense_2'),
                    alphasense_3 = request.POST.get('alphasense_3'),
                    alphasense_4 = request.POST.get('alphasense_4'),
                    alphasense_5 = request.POST.get('alphasense_5'),
                    alphasense_6 = request.POST.get('alphasense_6'),
                    alphasense_7 = request.POST.get('alphasense_7'),
                    alphasense_8 = request.POST.get('alphasense_8'),
                    reading_time = request.POST.get('reading_time'))
            point.save()
        except Exception as e:
            response_data['result'] = 'FAILED'
            response_data['msg'] = str(e)
            status = 400

    return HttpResponse(json.dumps(response_data), content_type="application/json", status=status)

@csrf_exempt
def secret_post_dylos(request):
    response_data = {}
    status = 400
    if request.method == "POST":
        print request.POST.items()
        response_data['result'] = 'OK'
        status = 200

        try:
            if ((int(float(request.POST.get('dylos_bin_1')) == -9999)) or
                    (int(float(request.POST.get('dylos_bin_2')) == -9999)) or
                    (int(float(request.POST.get('dylos_bin_3')) == -9999)) or
                    (int(float(request.POST.get('dylos_bin_4')) == -9999))):
                raise Exception('invalid entry -9999')

            point = Dylos(
                    node_id = request.POST.get('node_id'),
                    dylos_bin_1 = request.POST.get('dylos_bin_1'),
                    dylos_bin_2 = request.POST.get('dylos_bin_2'),
                    dylos_bin_3 = request.POST.get('dylos_bin_3'),
                    dylos_bin_4 = request.POST.get('dylos_bin_4'),
                    reading_time = request.POST.get('reading_time'))
            point.save()

            # update Latest
            try:
                ltst, created = Latest.objects.get_or_create(node_id=point.node_id)

                if created:
                    n = Node.objects.get(node_id=point.node_id)
                    ltst.node_id = n.node_id
                    ltst.name = n.name
                    ltst.latitude = n.latitude
                    ltst.longitude = n.longitude
                    ltst.indoor = n.indoor

                ltst.big_particles = point.big_particles
                ltst.small_particles = point.small_particles

                ltst.save()
            except:
                pass

        except Exception as e:
            response_data['result'] = 'FAILED'
            response_data['msg'] = str(e)
            status = 400

    return HttpResponse(json.dumps(response_data), content_type="application/json", status=status)

@csrf_exempt
def secret_post_alphasense(request):
    print "posting alphasense", request.POST
    response_data = {}
    status = 400
    if request.method == "POST":
        print request.POST.items()
        response_data['result'] = 'OK'
        status = 200

        try:
            if ((int(float(request.POST.get('alphasense_1')) == -9999)) or
                    (int(float(request.POST.get('alphasense_2')) == -9999)) or
                    (int(float(request.POST.get('alphasense_3')) == -9999)) or
                    (int(float(request.POST.get('alphasense_4')) == -9999)) or
                    (int(float(request.POST.get('alphasense_5')) == -9999)) or
                    (int(float(request.POST.get('alphasense_6')) == -9999)) or
                    (int(float(request.POST.get('alphasense_7')) == -9999)) or
                    (int(float(request.POST.get('alphasense_8')) == -9999))):
                raise Exception('invalid entry -9999')

            point = Alphasense(
                    node_id = request.POST.get('node_id'),
                    alphasense_1 = request.POST.get('alphasense_1'),
                    alphasense_2 = request.POST.get('alphasense_2'),
                    alphasense_3 = request.POST.get('alphasense_3'),
                    alphasense_4 = request.POST.get('alphasense_4'),
                    alphasense_5 = request.POST.get('alphasense_5'),
                    alphasense_6 = request.POST.get('alphasense_6'),
                    alphasense_7 = request.POST.get('alphasense_7'),
                    alphasense_8 = request.POST.get('alphasense_8'),
                    reading_time = request.POST.get('reading_time'))
            point.save()

            # update Latest
            try:
                ltst, created = Latest.objects.get_or_create(node_id=point.node_id)

                if created:
                    n = Node.objects.get(node_id=point.node_id)
                    ltst.node_id = n.node_id
                    ltst.name = n.name
                    ltst.latitude = n.latitude
                    ltst.longitude = n.longitude
                    ltst.indoor = n.indoor

                ltst.no = point.no
                ltst.no2 = point.no2
                ltst.co = point.co
                ltst.o3 = point.o3
                ltst.save()

            except:
                pass

        except Exception as e:
            response_data['result'] = 'FAILED'
            response_data['msg'] = str(e)
            status = 400

    return HttpResponse(json.dumps(response_data), content_type="application/json", status=status)

@csrf_exempt
def secret_post_met(request):
    response_data = {}
    status = 400
    if request.method == "POST":
        print request.POST.items()
        response_data['result'] = 'OK'
        status = 200

        try:
            if ((int(float(request.POST.get('temperature')) == -9999)) or
                    (int(float(request.POST.get('rh')) == -9999))):
                raise Exception('invalid entry -9999')

            point = Met(
                    node_id = request.POST.get('node_id'),
                    temperature = request.POST.get('temperature'),
                    rh = request.POST.get('rh'),
                    reading_time = request.POST.get('reading_time'))
            point.save()


            # update Latest
            try:
                ltst, created = Latest.objects.get_or_create(node_id=point.node_id)

                if created:
                    n = Node.objects.get(node_id=point.node_id)
                    ltst.node_id = n.node_id
                    ltst.name = n.name
                    ltst.latitude = n.latitude
                    ltst.longitude = n.longitude
                    ltst.indoor = n.indoor

                ltst.temperature = point.temperature
                ltst.rh = point.rh
                ltst.save()

            except:
                pass



        except Exception as e:
            response_data['result'] = 'FAILED'
            response_data['msg'] = str(e)
            status = 400

    return HttpResponse(json.dumps(response_data), content_type="application/json", status=status)




#------------------------------------------------------------
#  Post Entries for the front-end
#------------------------------------------------------------

@csrf_exempt
def get_latest_now_fix(request):
    nodes = Latest.objects.all()
    results = []

    for lnode in nodes:
        d = {}
        d['name'] = lnode.name
        d['node_id'] = lnode.node_id
        d['indoor'] = lnode.indoor
        d['latitude'] = lnode.latitude
        d['longitude'] = lnode.longitude
        d['temperature'] = lnode.temperature
        d['offline'] = lnode.offline
        d['rh'] = lnode.rh
        d['no'] = lnode.no
        d['no2'] = lnode.no2
        d['o3'] = lnode.o3
        d['co'] = lnode.co
        d['big_particles'] = lnode.big_particles
        d['small_particles'] = lnode.small_particles
        d['last_modified'] = str(lnode.last_modified)
        results.append(d)

    return HttpResponse(json.dumps(results), content_type="application/json", status=200)

@csrf_exempt
def graph_data(request):
    last_month = datetime.datetime.today()  - datetime.timedelta(days=30)
    if request.method == 'GET':
        sensor = request.GET.get('sensor')
        node_id = request.GET.get('node_id')
        if sensor and node_id:
            if sensor.lower() == 'dylossmall':
                return HttpResponse(
                        json.dumps([[int(time.mktime(a.timetuple())*1000),b] for a,b in Dylos.objects.filter(node_id=int(node_id)).filter(added_on__gte=last_month).values_list('added_on','small_particles').iterator()]) ,
                            content_type="application/json",
                            status=200)

            elif sensor.lower() == 'dylosbig':
                return HttpResponse(
                        json.dumps([[int(time.mktime(a.timetuple())*1000),b] for a,b in Dylos.objects.filter(node_id=int(node_id)).filter(added_on__gte=last_month).values_list('added_on', 'big_particles').iterator()]) ,
                            content_type="application/json",
                            status=200)
            elif sensor.lower() == 'no':
               return HttpResponse(
                        json.dumps([[int(time.mktime(a.timetuple())*1000),b] for a,b in Alphasense.objects.filter(node_id=int(node_id)).filter(added_on__gte=last_month).values_list('added_on','no').iterator()]) ,
                            content_type="application/json",
                            status=200)
            elif sensor.lower() == 'no2':
               return HttpResponse(
                        json.dumps([[int(time.mktime(a.timetuple())*1000),b] for a,b in Alphasense.objects.filter(node_id=int(node_id)).filter(added_on__gte=last_month).values_list('added_on','no2').iterator()]) ,
                            content_type="application/json",
                            status=200)
            elif sensor.lower() == 'o3':
               return HttpResponse(
                        json.dumps([[int(time.mktime(a.timetuple())*1000),b] for a,b in Alphasense.objects.filter(node_id=int(node_id)).filter(added_on__gte=last_month).values_list('added_on','o3').iterator()]) ,
                            content_type="application/json",
                            status=200)

            elif sensor.lower() == 'co':
               return HttpResponse(
                        json.dumps([[int(time.mktime(a.timetuple())*1000),b] for a,b in Alphasense.objects.filter(node_id=int(node_id)).filter(added_on__gte=last_month).values_list('added_on','co').iterator()]) ,
                            content_type="application/json",
                            status=200)

    return HttpResponse('No Match')



@csrf_exempt
def download_csv(request):
    if request.method == 'GET':
        sensor = request.GET.get('sensor')
        nodes= [int(x) for x in request.GET.get('node_ids').split(',')] if request.GET.get('node_ids') else []
        modeladmin = None
        queryset = None
        print " Nodes " , nodes , " sensor " ,sensor
        if sensor and nodes:
            if sensor.lower() == 'dylossmall':
                modeladmin = ModelAdmin(Dylos, None)
            elif sensor.lower() == 'dylosbig':
                modeladmin = ModelAdmin(Dylos, None)
            elif sensor.lower() == 'no':
                modeladmin = ModelAdmin(Alphasense, None)
            elif sensor.lower() == 'no2':
                modeladmin = ModelAdmin(Alphasense, None)
            elif sensor.lower() == 'o3':
                modeladmin = ModelAdmin(Alphasense, None)
            elif sensor.lower() == 'co':
                modeladmin = ModelAdmin(Alphasense, None)
            else:
                modeladmin = ModelAdmin(Dylos, None)

            queryset = modeladmin.model.objects.filter(node_id__in=nodes)

            return export_as_csv(modeladmin , request, queryset)

    return HttpResponse('An error occurred.',
            content_type="application/json",
            status=400)
