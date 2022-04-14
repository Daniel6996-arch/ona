from datetime import datetime, timedelta, timezone
from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import requests
from .models import StartDate,OnaData
import time
import threading
from time import sleep as wait
  
  
def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)  
   
def aslocaltimestr(utc_dt):
    return utc_to_local(utc_dt).strftime('%Y-%m-%d %H:%M:%S')   
   
def index():
    field_name = "start_date"
    obj = StartDate.objects.last()
    try: 
        field_object = StartDate._meta.get_field(field_name)
        start_date = field_object.value_from_object(obj) 
        start_date = start_date.strftime('%Y-%m-%d %H:%M:%S') 
    except:
        start_date =datetime(1970,1,1)
        
       
    url = 'https://api.ona.io/api/v1/data/661447.json?query={"_submission_time":{"$gte":"%s"}}' %start_date
    username = "dantekariuki"
    password = "Kariyki6996@"
    response = requests.get(url, auth=(username,password))
    data = response.json()
    
    
    for i in data:
        ona_data = OnaData(
           name = i['Name'],
           age = i['Age'],
           status = i['Marital_Status'],
           employment = i['Employment'],
           gender = i['Gender']
        )
        names = OnaData.objects.all().values_list('name', flat=True) 
        end_date = StartDate(start_date = datetime.today())
        end_date.save()  
        if ona_data.name in names:
            print("Name already saved")
        else:
            ona_data.save() 
    
def pull_interval():
    wait(0)
    while True:
        thr = threading.Thread(target=index)
        thr.start()
        wait(120)
 
    
    