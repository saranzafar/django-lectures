from django.shortcuts import render
from student.forms import Register
from django.http import HttpResponseRedirect
from student.models import Profile

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            clean_form_data = form.cleaned_data
            
            data = Profile.objects.create(
                first_name=clean_form_data['first_name'],
                email=clean_form_data['email'],
                password=clean_form_data['password']  # Ensure to hash passwords in production
            )
            data.save()            
            return HttpResponseRedirect('/student/success/')
        # form = Register()  # Reset the form after successful submission

    else:
        form = Register()
    return render(request, 'student/register.html', {'form': form})

def success(request):
    return render(request, 'student/success.html')