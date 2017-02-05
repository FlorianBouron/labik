from django.shortcuts import render
from .models import Book


def index(request):
    last_books = Book.objects.all().order_by('-published_date')[:3]
    return render(request, 'website/index.html', {'last_books': last_books})
