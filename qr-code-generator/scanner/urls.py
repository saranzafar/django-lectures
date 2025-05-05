from django.urls import path
from .views import GenerateQRView, ScanQRView

app_name = 'scanner'

urlpatterns = [
    path('generate/', GenerateQRView.as_view(), name='generate_qr'),
    path('scan/',    ScanQRView.as_view(),    name='scan_qr'),
]
