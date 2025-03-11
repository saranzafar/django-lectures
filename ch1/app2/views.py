from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def myFunctionApp2(request):
    return HttpResponse("Hello Django")