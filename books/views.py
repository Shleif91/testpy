from django.shortcuts import render


def post_list(request):
    return render(request, 'books/post_list.html', {})


def books_list(request):
    return render(request, 'books/books_list.html', {})
