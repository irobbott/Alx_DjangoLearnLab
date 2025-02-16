
---

### **delete.md**  
```md
# Deleting a Book Instance

## Command:
```python
from bookshelf.models import Book

# Fetch the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion by retrieving all books
Book.objects.all()

