from django.http import HttpResponse
#utilities
from datetime import datetime



def hello_world(request):
    return HttpResponse('Hi, current server time is {nowTime}'.format(
        nowTime = datetime.now().strftime('%b %dth, %Y %H:%M hrs')
    ))
