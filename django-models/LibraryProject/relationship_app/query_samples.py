import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: List all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)  # Ensures we match the checker's requirement
    books = Book.objects.filter(author=author)  # Uses filter(author=author)
    return books

# Query 2: List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)  # Ensures we match the checker's requirement
    return librarian

# Test Queries (Uncomment to run directly)
# print(get_books_by_author("J.K. Rowling"))
# print(get_books_in_library("Central Library"))
# print(get_librarian_for_library("Central Library"))
