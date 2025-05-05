from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def landing(request):
    return render(request, 'core/landing.html')

# def generate_qr(request):
#     return render(request, 'core/generate_qr.html')

# def scan_qr(request):
#     return render(request, 'core/scan_qr.html')
