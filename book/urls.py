from django.urls import path
from . import views

urlpatterns = [
    path('Привет/', views.hello_view, name='Привет'),
    path('book/', views.book_view, name='book'),
]