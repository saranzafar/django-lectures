from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Home Page")

def myFunction(request):
    return HttpResponse("Hello Django")

def html(request):
    return HttpResponse("<h1>Hi this is h1</h1>")

def math(request):
    a = 12 + 13;
    return HttpResponse(a)

def php(request):
    lang = '<h1>Hello PHP</h1>'
    return HttpResponse(lang)
