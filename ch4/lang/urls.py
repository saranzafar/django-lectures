from django.urls import path
from lang.views import home

urlpatterns = [
   path('', home),   
]
