from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from data.models import DataPoint, Met, Alphasense, Dylos, AQI, Node
import json
import datetime

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

            point = Dylos(
                    node_id = request.POST.get('node_id'),
                    dylos_bin_1 = request.POST.get('dylos_bin_1'),
                    dylos_bin_2 = request.POST.get('dylos_bin_2'),
                    dylos_bin_3 = request.POST.get('dylos_bin_3'),
                    dylos_bin_4 = request.POST.get('dylos_bin_4'),
                    reading_time = request.POST.get('reading_time'))
            point.save()
        except Exception as e:
            response_data['result'] = 'FAILED'
            response_data['msg'] = str(e)
            status = 400

    return HttpResponse(json.dumps(response_data), content_type="application/json", status=status)

@csrf_exempt
def secret_post_alphasense(request):
    response_data = {}
    status = 400
    if request.method == "POST":
        print request.POST.items()
        response_data['result'] = 'OK'
        status = 200

        try:

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

            point = Met(
                    node_id = request.POST.get('node_id'),
                    temperature = request.POST.get('temperature'),
                    rh = request.POST.get('rh'),
                    reading_time = request.POST.get('reading_time'))
            point.save()
        except Exception as e:
            response_data['result'] = 'FAILED'
            response_data['msg'] = str(e)
            status = 400

    return HttpResponse(json.dumps(response_data), content_type="application/json", status=status)




#------------------------------------------------------------
#  Post Entries for the front-end
#------------------------------------------------------------

@csrf_exempt
def get_latest(request, hour=False,  day=False, week=False):
    if week or day or hour:
        end_date = datetime.datetime.now()
        if week:
            start_date = end_date - datetime.timedelta(days=7)
        elif day:
            start_date = end_date - datetime.timedelta(hours=24)
        else:
            # past hour
            start_date = end_date - datetime.timedelta(minutes=60)

        # return current latest
        node_ids = range(1,26)
        results = []

        for node_id in node_ids:
            latest = AQI.objects.filter(node_id=node_id).filter(added_on__range=(start_date, end_date))
            if latest:
                results.extend(latest)
        return HttpResponse(json.dumps(results), content_type="application/json", status=200)

    else:
        # return current latest single element
        node_ids = range(1,26)
        results = []
        for node_id in node_ids:
            try:
                latest = AQI.objects.filter(node_id=node_id).latest('id')
                if latest:
                    results.append(latest)
            except:
                pass
        return HttpResponse(json.dumps(results), content_type="application/json", status=200)


@csrf_exempt
def get_latest_now_fix(request):
    nodes = Node.objects.all()
    results = []
    for node in nodes:
        d = {}
        d['node_id'] = node.node_id
        d['name'] = node.name
        d['latitude'] = node.latitude
        d['longitude'] = node.longitude
        d['indoor'] = node.indoor

        try:
            dylos = Dylos.objects.filter(node_id=node.node_id).latest('added_on')
            if dylos:
                d['dylos_bin_1'] = dylos.dylos_bin_1
                d['dylos_bin_2'] = dylos.dylos_bin_2
                d['dylos_bin_3'] = dylos.dylos_bin_3
                d['dylos_bin_4'] = dylos.dylos_bin_4
        except:
            pass

        try:
            alphasense = Alphasense.objects.filter(node_id=node.node_id).latest('added_on')

            if alphasense:
                NO2_OP1 = alphasense.alphasense_1
                NO2_OP2 = alphasense.alphasense_2
                #d['no2'] = ((WE-WE_Vo)-(Aux-AUX_Vo))/sensitivity
                d['no2'] = 232
                O3_OP1= alphasense.alphasense_3
                O3_OP2 = alphasense.alphasense_4
                d['o3'] = 423
                CO_OP1= alphasense.alphasense_5
                CO_OP2= alphasense.alphasense_6
                d['co'] = 234
                NO_OP1= alphasense.alphasense_7
                NO_OP2= alphasense.alphasense_8
                d['no'] = 236
        except:
            pass

        results.append(d)

    return HttpResponse(json.dumps(results), content_type="application/json", status=200)
