"""
URL configuration for ch1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from app1 import views as ap1
# from app2 import views as ap2

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', ap1.home,name='home'),
#     path('app/', ap1.myFunction,name='myfunction'),
#     path('html/', ap1.html,name='html'),
#     path('math/', ap1.math,name='math'),
#     path('php/', ap1.php,name='php'),
    
#     path('app2/', ap2.myFunctionApp2,name='myFunctionApp2'),
# ]

# Alternative 
from django.contrib import admin
from django.urls import path
from app1.views import home, html, math,myFunction,php
from app2.views import myFunctionApp2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('app/', myFunction,name='myfunction'),
    path('html/', html,name='html'),
    path('math/', math,name='math'),
    path('php/', php,name='php'),
    
    path('app2/', myFunctionApp2,name='myFunctionApp2'),
]
