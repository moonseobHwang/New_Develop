from django.shortcuts import render
from django.http import HttpResponse
import requests
from pymongo import MongoClient
# Create your views here.

def listwithmongo(request):
    data = request.GET.copy()
    with MongoClient('mongodb://13.125.191.54:53368/') as client:
        workbs4 = client.workbs4
        result = list(workbs4.sampleCollection.find({}))
        data['page_obj']=result
    return render(request, 'board/listwithmongo.html', context=data)

def workwithmongo(request):
    data2 = request.GET.copy()
    with MongoClient('mongodb://13.125.191.54:53368/') as client:
        work = client.work
        result = list(work.sampleCollection.find({}))
        data2['page_obj2']=result
    return render(request, 'board/workwithmongo.html', context=data2)