
from django.http import HttpResponse, JsonResponse
#utilities
from datetime import datetime
import json


def hello_world(request):
    return HttpResponse('Hi, current server time is {nowTime}'.format(
        nowTime = datetime.now().strftime('%b %dth, %Y %H:%M hrs')
    ))


def hi(request):
    return HttpResponse('Hi!')


def get_params_json(request):
    try:
        params = request.GET['numbers']
    except:
        return HttpResponse(
            'Debe ingresar el parametro numbers con un conjunto de números p.e. ?numbers=10,30,4,50,2')
    responseArray = []
    for value in params.split(','):
        try:
            responseArray.append(int(value))
        except:
            return HttpResponse(
                'El parámetro numbers debe contener solo números')
    responseArray.sort()
    return JsonResponse(responseArray, safe=False)
