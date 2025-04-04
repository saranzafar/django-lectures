from core.views import home, menu, reservation, tracking, contact
from django.urls import path
# Importing the necessary modules for URL routing

urlpatterns = [
    path('', home, name='home'),  
    path('menu/', menu, name='menu'),
    path('reservation/', reservation, name='reservation'),
    path('tracking/', tracking, name='tracking'),
    path('contact/', contact, name='contact'),
]
