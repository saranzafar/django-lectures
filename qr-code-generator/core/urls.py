from django.urls import path
from core.views import home, landing

urlpatterns = [
    path('', home, name='home'),
    path('landing/', landing, name='landing'),
    # path('generate_qr', generate_qr, name='generate_qr'),
    # path('scan_qr', scan_qr, name='scan_qr'),
    
]
