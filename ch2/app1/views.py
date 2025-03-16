from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_django(req, **kawrgs):
    status = kawrgs.get('status','Not Allowed')
    return HttpResponse(f'<h1>Hello Django {status} </h1>')
