# Retrieving a Book Instance

## Command:
```python
from bookshelf.models import Book

# Retrieve the book by title
book = Book.objects.get(title="1984")

# Display the book details
book
