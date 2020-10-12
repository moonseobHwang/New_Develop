from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def home(request):
    return HttpResponse("Hello, Django")

def taskstring(request):
    result = "Rest API string!"
    return HttpResponse(result, content_type="text/plain")

def responsewithhtml(request):
    # data={'first':'Sanghun','second':'Oh'}
    data = dict()
    data["first"] = request.GET['first']
    data["second"] = request.GET['second']
    return render(request,'hello/responsewithhtml.html',context=data)

def form(request):
    return render(request,'hello/requestsform.html')
