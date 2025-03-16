from django.urls import path
from app2.views import my_app2

urlpatterns = [
    path('dj/', my_app2),
]
