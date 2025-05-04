from django.shortcuts import render
from student.forms import Register
from django.http import HttpResponseRedirect

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']  
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            return HttpResponseRedirect('/student/register')
    
    form = Register()
    return render(request, 'student/register.html', {'form': form})