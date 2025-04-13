from django.urls import path
from student.views import register, success

urlpatterns = [
    path('register/', register, name='register'),
    path('success/', success, name='success'),
]