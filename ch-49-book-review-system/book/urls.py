from django.urls import path
from book import views

urlpatterns = [
    path('book/new/', views.book_create,name = "book-create" ),
]
