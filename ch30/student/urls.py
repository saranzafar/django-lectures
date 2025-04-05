from django.urls import path
from student.views import registration, login

urlpatterns = [
    path('register/',registration, name= 'register'),
    path('login/',login, name= 'Login')
]
