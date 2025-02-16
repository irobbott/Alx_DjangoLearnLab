# Retrieving a Book Instance

## Command:
```python
from bookshelf.models import Book

# Retrieving all books
books = Book.objects.all()

# Display the first book
books.first()

