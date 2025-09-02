from django.urls import path, include
from blog.views import home, blog_list, blog_detail

urlpatterns = [
    path('', home, name='home'),
    path("blogs/", blog_list, name="blog_list"),
    path("blogs/<slug:slug>/", blog_detail, name="blog_detail"),
]
