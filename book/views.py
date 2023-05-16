from django.http import HttpResponse
from django.shortcuts import render
from book.models import Book

def hello_view(request):
    return HttpResponse("Привет, это мой первый дз по джанго")

#Список книг на веб странице(логика отображения)
def book_view(request):
    book = Book.objects.all()
    return render(request, 'book.html',{'book': book})

