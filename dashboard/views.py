from django.shortcuts import render , redirect
import requests
from django.contrib import messages
from .models import Dash
# Create your views here.
def dashboard(request):
    response =  requests.get('https://api.thingspeak.com/channels/1377104/feeds.json?results=2').json()
    data = response['feeds']
    context = {
        'data': data
    }
    if data[0]['field5']==1:
        messages.error(request,"Fire has been Detected")
    return render(request,'dashboards/dashboard.html',context)
    