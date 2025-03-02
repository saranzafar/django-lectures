from django.url import path
from core.views import home

urlpatterns = [
    path('',home)
]