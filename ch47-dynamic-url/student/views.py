from django.shortcuts import render
from django.contrib import messages
from .forms import StudentRegistration 

# Create your views here.
def home(request):
    return render(request, 'student/home.html')

# def profile(request, my_id, my_class):
#     student = {'id': my_id, 'class': my_class}
#     return render(request, 'student/profile.html', student)

def profile(request, year):
    return render(request, 'student/profile.html', {'year': year})

def message(request):
    # messages.add_message(request, messages.SUCCESS, 'Your account has been created!')
    # messages.add_message(request, messages.INFO, 'This is info')
    # messages.add_message(request, messages.WARNING, 'This is warning')
    # messages.add_message(request, messages.ERROR, 'This is Error')

    # Alternative 
    messages.success(request, 'This is Success')
    messages.info(request, 'This is Info')
    messages.warning(request, 'This is Warning')
    messages.error(request, 'This is Error')
    messages.debug(request, 'This is Debug')
    messages.set_level(request, messages.DEBUG)
    print(messages.get_level(request))
    messages.debug(request, 'This is Debug after set!!!')

    return render(request, 'student/messages.html')

def register(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered Successfully!')

    else:
        form = StudentRegistration()

    return render(request, 'student/register.html',{'form':form})