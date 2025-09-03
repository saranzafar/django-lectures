from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'student/home.html')

# def profile(request, my_id, my_class):
#     student = {'id': my_id, 'class': my_class}
#     return render(request, 'student/profile.html', student)

def profile(request, year):
    return render(request, 'student/profile.html', {'year': year})

