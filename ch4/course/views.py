from django.shortcuts import render
from datetime import datetime

# Create your views here.
def learn_django(req):
    date = datetime.now()
    return render(req,'course/learn_django.html',context={
        'name':'Django',
        'description':'lorem libsum dkfg sdkfgj s  wer rwsfv sd sdf s fsdwefw',
        'date':date,
        'p1':103040400,
        'p2':33.4545,
        'p3':434.44445464,
        'items':[
            {'name':'django','price':100},
            {'name':'python','price':200},
            {'name':'flask','price':300},
            {'name':'html','price':400},
        ],
        'is_active':True,
        'is_active1':False,
    })
    
def static_file(req):
    return render (req,'course/static_file.html')    

def home(req):
    return render (req,'core/home.html')
    