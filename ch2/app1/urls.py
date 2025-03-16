from django.urls import path
from app1.views import learn_django

urlpatterns = [
    path('dj/', learn_django),
]
