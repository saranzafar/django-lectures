from django.urls import path
from course.views import learn_django, learn_fastapi

urlpatterns = [
    path('dj/',learn_django),
    path('fa/',learn_fastapi)
]
