from django.shortcuts import render
from student.models import Profile

# Create your views here.
def all_data(req):
   students =  Profile.objects.all()
   print(students)
   return render(req, 'student/all.html', {'students': students})

def single_data(req):
   # student =  Profile.objects.get(pk=1)
   # student =  Profile.objects.get(id=1)
   student =  Profile.objects.get(name='ali')
   print(student)
   return render(req, 'student/single.html', {'student': student})