from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def my_app2(req):
    return HttpResponse(f'<h1>My App 2 </h1>')

