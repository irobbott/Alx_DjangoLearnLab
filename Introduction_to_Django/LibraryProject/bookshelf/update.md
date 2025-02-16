
---

### **update.md**  
```md
# Updating a Book Instance

## Command:
```python
from bookshelf.models import Book

# Fetch the book instance
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm the update
book

