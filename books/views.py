from django.shortcuts import render
from .models import Book

def post_list(request):
    return render(request, 'books/post_list.html', {})


def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'all_books': books})
