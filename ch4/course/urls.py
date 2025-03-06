from django.urls import path
from django.contrib import admin
from course.views import learn_django, static_file, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learn_django/', learn_django, name='learn_django'),   
    path('static_file/', static_file, name='static_file'),   
    path('course/', home),   
]
