from django.shortcuts import render

# Create your views here.
def learn_django (req):
    seats = 10
    coursename = {'cname': 'Django','version':'5.2.1','st':seats}
    # return render(req,'course/learn_django.html',context= coursename)
    # return render(req,'course/learn_django.html',{'cname': 'Python Django'})
    return render(req,'course/learn_django.html',coursename)

def learn_fastapi (req):
    return render(req,'course/fastapi.html')