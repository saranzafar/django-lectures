from django.shortcuts import render
from student.forms import Registration, Login

# Create your views here.
def registration(req):
    # form = Registration()
    form = Registration(field_order=['email','city'])
    return render(req, 'student/registration.html',{'form': form})

def login(req):
    form = Login()
    # form = Login(auto_id='saran_%s') # saran_forst_name
    # form = Login(auto_id=True) # first name -> name
    # form = Login(auto_id=False)# No Lable Tag
    # form = Login(auto_id='saran')# This Consider as True
    
    # form = Login(label_suffix='A') # After Lable there comes 'A' i.e. Email - > EmailA
    # form = Login(label_suffix='') # No Colon

    # form = Login(initial={'email':'example@gmail.com', 'password':'abc'}) # initial value pre set

    return render(req, 'student/login.html',{'form': form})