from django.shortcuts import render

# Create your views here.
def django(request):
    return render(request, 'course/django.html')

def python(request):
    return render(request, 'course/python.html')