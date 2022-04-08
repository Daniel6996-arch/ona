from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from .models import StartDate,EndDate,OnaData

# Create your views here.
def index(request):
    start_date = StartDate.objects.first()
    end_date = EndDate.objects.first()
    url = 'https://api.ona.io/api/v1/data/661447.json?query={"_submission_time":{"$gte":"2020-01-01","$lte":"2022-04-09"}}'
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
    #    for i in ona_data:
    #     obj, created = OnaData.objects.get_or_create(i);  
       #ona_data.save()
       all_data = OnaData.objects.all()
       for se in all_data.iterator():
           if se.name.exists():
            print(se)
    
    return render(request, 'index.html', {'data':data})
