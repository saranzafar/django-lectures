from django.urls import path
from course.views import django, python

urlpatterns = [
    path('dj/', django, name='django'),
    path('py/', python, name='python'),
]