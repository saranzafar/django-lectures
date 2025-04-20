from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'data': 'Hello I am django developer and I am also a python developer'}
    return render(request, 'student/home.html', context)