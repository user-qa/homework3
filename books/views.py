from django.shortcuts import render

from books.models import BookModel


def books_info_view(request):
    books = BookModel.objects.all()
    context = {
        'books_list': books
    }
    return render(request, 'books.html', context)