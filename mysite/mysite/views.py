from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render_to_response
from django.template.loader import get_template
import datetime

def current_time(request):
    now=datetime.datetime.now()
    t=get_template('base.html')
    html=t.render(Context({'now':now}))
    return HttpResponse(html)

def hours_ahead(request,offset):
    offset=int(offset)
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    
    return render_to_response('b2.html',Context({'offset':offset,'dt':dt}))