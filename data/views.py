from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from data.models import DataPoint, Met, Alphasense, Dylos, AQI
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
            latest = AQI.objects.filter(node_id=node_id).latest('id')
            if latest:
                results.append(latest)

        return HttpResponse(json.dumps(results), content_type="application/json", status=200)
