from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.decorators import permission_required

# Create your views here.
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    return render(request, 'bookshelf/create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return render(request, 'bookshelf/delete_book.html')

class BookListView(PermissionRequiredMixin, ListView):
    model = Book
    template_name = "bookshelf/book_list.html"
    context_object_name = "books"
    permission_required = "bookshelf.can_view"

    # Securely fetching a book using ORM
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "bookshelf/book_detail.html", {"book": book})

# Secure search functionality
def book_search(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    return render(request, 'bookshelf/book_list.html', {'books': books, 'query': query})